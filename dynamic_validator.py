import json
from jsonschema import validate, ValidationError
from simple_graphql_parser import SimpleGraphQLParser
from simple_query_parser import SimpleQueryParser

class DynamicGraphQLValidator:
    def __init__(self, schema_file_path):
        with open(schema_file_path, 'r') as f:
            self.sdl_content = f.read()
        
        self.schema_parser = SimpleGraphQLParser(self.sdl_content)
        self.query_parser = SimpleQueryParser()

        self.scalar_map = {
            'String': {'type': 'string'},
            'ID': {'type': 'string'},
            'Int': {'type': 'integer'},
            'Float': {'type': 'number'},
            'Boolean': {'type': 'boolean'},
            'Long': {'type': 'integer'},
            'BigInt': {'type': 'integer'},
            'BigDecimal': {'type': 'number'},
            'OffsetDateTime': {'type': 'string'},
            'JSON': {'type': 'object'},
        }

    def validate(self, query_str, response_data, variables=None):
        parsed_query = self.query_parser.parse(query_str)
        
        if variables is not None:
            self._validate_variables(parsed_query['variables'], variables)

        self._validate_response(parsed_query, response_data)
        return True

    def _validate_variables(self, var_defs, variables_data):
        properties = {}
        required = []

        for var_name, var_type_str in var_defs.items():
            var_schema = self._build_input_schema(var_type_str)
            properties[var_name] = var_schema
            if var_type_str.endswith('!'):
                required.append(var_name)

        variables_schema = {
            "type": "object",
            "properties": properties,
            "required": required,
            "additionalProperties": False 
        }

        try:
            validate(instance=variables_data, schema=variables_schema)
        except ValidationError as e:
            path = "root"
            if e.path:
                path = ".".join([str(p) for p in e.path])
            raise ValidationError(f"Variablen-Validierungsfehler bei '${path}': {e.message}")

    def _build_input_schema(self, type_str):
        # 1. Wrapper Analyse
        is_list = False
        is_outer_non_null = False
        is_inner_non_null = False # Default: Innere Items sind nullable ([String])

        clean_type = type_str
        if clean_type.endswith('!'):
            is_outer_non_null = True
            clean_type = clean_type[:-1]
        
        if clean_type.startswith('[') and clean_type.endswith(']'):
            is_list = True
            clean_type = clean_type[1:-1]
            if clean_type.endswith('!'):
                is_inner_non_null = True # [String!] -> Items nicht nullable
                clean_type = clean_type[:-1]
            else:
                is_inner_non_null = False # [String] -> Items nullable
        
        # 2. Schema bauen
        schema = {}

        if clean_type in self.scalar_map:
            schema = self.scalar_map[clean_type].copy()
        elif clean_type in self.schema_parser.definitions['scalars']:
            schema = {"type": ["string", "integer"]}
        elif clean_type in self.schema_parser.definitions['enums']:
            schema = {
                "type": "string",
                "enum": self.schema_parser.definitions['enums'][clean_type]
            }
        elif clean_type in self.schema_parser.definitions['inputs']:
            input_def = self.schema_parser.definitions['inputs'][clean_type]
            props = {}
            req_fields = []
            for field_name, field_info in input_def.items():
                props[field_name] = self._build_input_schema(field_info['type'])
                if field_info['type'].endswith('!'):
                    req_fields.append(field_name)
            schema = {
                "type": "object",
                "properties": props,
                "required": req_fields,
                "additionalProperties": False
            }
        else:
            schema = {"type": "object"}

        # 3. Wrapper anwenden
        if is_list:
            if not is_inner_non_null:
                self._make_nullable(schema)
            
            schema = {"type": "array", "items": schema}
        
        if not is_outer_non_null:
             self._make_nullable(schema)

        return schema

    def _validate_response(self, parsed_query, response_data):
        op_type = parsed_query['type'] 
        selection_tree = parsed_query['fields']

        root_type_def = None
        root_name = ""
        if op_type == 'mutation':
            root_type_def = self.schema_parser.get_mutation_type()
            root_name = "Mutation"
        else:
            root_type_def = self.schema_parser.get_query_type()
            root_name = "Query"

        if not root_type_def:
             raise ValueError(f"Schema hat keinen Typ '{root_name}' definiert.")

        properties = {}
        for field_name, sub_selection in selection_tree.items():
            if field_name not in root_type_def:
                 raise ValueError(f"Feld '{field_name}' existiert nicht im Typ '{root_name}'.")

            field_def = root_type_def[field_name]
            properties[field_name] = self._build_field_schema(field_def['type'], sub_selection)

        dynamic_schema = {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "properties": properties,
                    "required": list(properties.keys()),
                    "additionalProperties": False
                }
            },
            "required": ["data"]
        }
        
        validate(instance=response_data, schema=dynamic_schema)

    def _build_field_schema(self, type_str, selection_tree):
        # 1. Wrapper Analyse
        is_list = False
        is_outer_non_null = False
        is_inner_non_null = False

        clean_type = type_str
        if clean_type.endswith('!'):
            is_outer_non_null = True
            clean_type = clean_type[:-1]
        
        if clean_type.startswith('[') and clean_type.endswith(']'):
            is_list = True
            clean_type = clean_type[1:-1]
            if clean_type.endswith('!'):
                is_inner_non_null = True
                clean_type = clean_type[:-1]
            else:
                is_inner_non_null = False

        # 2. Schema bauen
        schema = {}

        if clean_type in self.scalar_map:
            schema = self.scalar_map[clean_type].copy()
        
        elif clean_type in self.schema_parser.definitions['scalars']:
            schema = {"type": ["string", "integer"]}

        elif clean_type in self.schema_parser.definitions['enums']:
            schema = {
                "type": "string",
                "enum": self.schema_parser.definitions['enums'][clean_type]
            }

        elif clean_type in self.schema_parser.definitions['types']:
            type_def = self.schema_parser.definitions['types'][clean_type]
            
            if selection_tree is None:
                schema = {"type": "object"}
            else:
                props = {}
                for sub_field, sub_sub_selection in selection_tree.items():
                    if sub_field == '__typename':
                        props['__typename'] = {"type": "string"}
                        continue

                    if sub_field not in type_def:
                        raise ValueError(f"Feld '{sub_field}' existiert nicht im Typ '{clean_type}'.")
                    
                    sub_field_def = type_def[sub_field]
                    props[sub_field] = self._build_field_schema(sub_field_def['type'], sub_sub_selection)

                schema = {
                    "type": "object",
                    "properties": props,
                    "required": list(props.keys()),
                    "additionalProperties": False
                }
        else:
             schema = {"type": "object"}

        # 3. Wrapper anwenden
        if is_list:
            if not is_inner_non_null:
                self._make_nullable(schema)

            schema = {
                "type": "array",
                "items": schema
            }
        
        if not is_outer_non_null:
             self._make_nullable(schema)

        return schema

    def _make_nullable(self, schema):
        if "type" in schema:
            if isinstance(schema["type"], str):
                schema["type"] = [schema["type"], "null"]
            elif isinstance(schema["type"], list) and "null" not in schema["type"]:
                schema["type"].append("null")
        elif "enum" in schema:
            schema = {"oneOf": [schema, {"type": "null"}]}
        elif "oneOf" in schema:
            schema["oneOf"].append({"type": "null"})
        elif "properties" in schema: 
            schema = {"oneOf": [schema, {"type": "null"}]}
            