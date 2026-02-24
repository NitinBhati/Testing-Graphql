import json
import pprint
from simple_graphql_parser import SimpleGraphQLParser

# --- DEFAULTS ---
DEFAULT_STRATEGIES = {
    "SCALARS": {
        "IMSI": "262199099999999",
        "ICCID": None,
        "String": "test_string", # I have simOrderState -> id: "MvoLBBzZDBJH", but this is a type string
        "Boolean": False,
        "Int": 0,
        "OffsetDateTime": "2024-01-01T12:00:00Z",
        "ID": "ID_PLACEHOLDER",
        "SimChangeId": "E1ELAqpIEDHmxkg"
    },
    "OBJECTS": {
        "PagingInput": {
            "first": 10,
            "after": None,
            "before": None,
            "last": None,
            "limit": None,
            "offset": 0
        },
        "SimInput": {
            "imsi": "262199099999999",
            "iccid": None
        },
        "BusinessUnitDetailsParametersInput": {
            "input": {
                "businessUnitId": "Bf0HAwAAAYCAAE"
            }
        },
        "InvoiceDownloadParametersInput": {
            "input": {
                "invoiceId": "cd8ce2db0e0a544"
            }
        }
    }
}

class QueryGenerator:
    def __init__(self, parser, defaults):
        self.parser = parser
        self.defaults = defaults
        self.max_depth = 3
        self.connection_depth_allowance = 2

    def generate_all(self):
        queries = self._process_ops(self.parser.get_query_type(), "query")
        mutations = self._process_ops(self.parser.get_mutation_type(), "mutation")
        return {"queries": queries, "mutations": mutations}

    def _process_ops(self, type_def, op_name):
        results = {}
        if not type_def: return results

        for field_name, details in type_def.items():
            args = details.get("args", {})
            return_type = details["type"]

            query_str, var_defs = self._build_query_string(field_name, args, return_type, op_name)
            variables = self._build_variables(args)

            results[field_name] = {
                "query": query_str,
                "variables": variables
            }
        return results

    def _build_query_string(self, field_name, args, return_type, op_name):
        var_parts = []
        arg_parts = []

        for arg_name, arg_details in args.items():
            arg_type = arg_details["type"]
            var_parts.append(f"${arg_name}: {arg_type}")
            arg_parts.append(f"{arg_name}: ${arg_name}")

        var_str = f"({', '.join(var_parts)})" if var_parts else ""
        arg_str = f"({', '.join(arg_parts)})" if arg_parts else ""

        selection = self._generate_selection(return_type, depth=0)

        return f"{op_name} {field_name}{var_str} {{\n  {field_name}{arg_str} {selection}\n}}", var_parts

    def _generate_selection(self, type_name, depth):
        clean = type_name.replace("!", "").replace("[", "").replace("]", "")

        if clean in self.parser.definitions["scalars"] or \
           clean in self.parser.definitions["enums"] or \
           clean in ["String", "Int", "Boolean", "Float", "ID", "Long", "BigDecimal", "JSON", "BigInt"]:
            return ""

        effective_max_depth = self.max_depth
        if "Connection" in clean or "Edge" in clean:
            effective_max_depth += self.connection_depth_allowance

        if depth >= effective_max_depth:
            return "{ __typename }"

        if clean in self.parser.definitions["types"]:
            fields = self.parser.definitions["types"][clean]
            selected_blocks = []

            for fname, fdetails in fields.items():
                ftype = fdetails["type"]
                clean_ftype = ftype.replace("!", "").replace("[", "").replace("]", "")

                # Argumente im Selection Set überspringen (zu komplex für Auto-Gen)
                if fdetails.get("args") and len(fdetails["args"]) > 0:
                     continue

                if self._is_leaf(clean_ftype):
                    selected_blocks.append(fname)
                else:
                    is_important_structure = False
                    if "Connection" in clean and fname in ["edges", "pageInfo"]:
                        is_important_structure = True
                    if "Edge" in clean and fname in ["node", "cursor"]:
                        is_important_structure = True

                    if is_important_structure or depth < (effective_max_depth - 1):
                        sub_select = self._generate_selection(clean_ftype, depth + 1)
                        if sub_select:
                            selected_blocks.append(f"{fname} {sub_select}")

            if not selected_blocks:
                return "{ __typename }"

            return "{\n    " + "\n    ".join(selected_blocks) + "\n  }"

        return ""

    def _is_leaf(self, type_name):
        return (type_name in self.parser.definitions["scalars"] or
                type_name in self.parser.definitions["enums"] or
                type_name in ["String", "Int", "Boolean", "Float", "ID", "Long", "BigDecimal", "JSON", "BigInt"])

    def _build_variables(self, args):
        vars_dict = {}
        for arg_name, details in args.items():
            raw_type = details["type"]
            vars_dict[arg_name] = self._get_dummy_value(raw_type)
        return vars_dict

    def _get_dummy_value(self, type_str, visited_inputs=None):
        if visited_inputs is None: visited_inputs = set()

        is_required = type_str.endswith("!")

        clean = type_str.replace("!", "")
        is_list = clean.startswith("[")
        if is_list: clean = clean[1:-1]
        if clean.endswith("!"): clean = clean[:-1]

        val = None

        # 1. Configured Objects
        if clean in self.defaults["OBJECTS"]:
            # Wir nehmen den konfigurierten Wert
            val = self.defaults["OBJECTS"][clean]

        # 2. Configured Scalars
        elif clean in self.defaults["SCALARS"]:
            if is_required:
                val = self.defaults["SCALARS"][clean]
            else:
                val = None

        # 3. Enums
        elif clean in self.parser.definitions["enums"]:
            if is_required:
                val = self.parser.definitions["enums"][clean][0]
            else:
                val = None

        # 4. Inputs
        elif clean in self.parser.definitions["inputs"]:
            if clean in visited_inputs:
                return {}

            visited_inputs.add(clean)
            val = {}
            for fname, fdetails in self.parser.definitions["inputs"][clean].items():
                field_val = self._get_dummy_value(fdetails["type"], visited_inputs.copy())
                val[fname] = field_val

            # Collapse Logic
            if not is_required:
                is_empty = True
                for v in val.values():
                    if v is not None:
                        is_empty = False
                        break
                if is_empty:
                    return None

        if is_list:
            if val is None:
                return []
            return [val]

        return val

if __name__ == "__main__":
    try:
        with open("schema.graphql", "r") as f:
            content = f.read()

        parser = SimpleGraphQLParser(content)
        generator = QueryGenerator(parser, DEFAULT_STRATEGIES)
        all_ops = generator.generate_all()

        with open("generated_queries_v2.py", "w") as f:

            f.write("import datetime\n")
            f.write("# Automatisch generierte Datei - Bitte nicht manuell ändern, sondern Generator anpassen\n\n")

            f.write("# --- VERWENDETE DEFAULTS ---\n")
            f.write("DEFAULTS = " + pprint.pformat(DEFAULT_STRATEGIES, width=120) + "\n\n")

            f.write("# --- QUERIES ---\n")
            f.write("QUERIES = " + pprint.pformat(all_ops["queries"], width=120) + "\n\n")

            f.write("# --- MUTATIONS ---\n")
            f.write("MUTATIONS = " + pprint.pformat(all_ops["mutations"], width=120) + "\n")

        print("Erfolg: generated_queries_v2.py generiert.")
        print("  - Python Syntax korrigiert (None/False)")
        print("  - Nesting Probleme behoben (durch pprint)")
    except Exception as e:
        print(f"Fehler: {e}")
        import traceback
        traceback.print_exc()[