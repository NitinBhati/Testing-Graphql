from graphql import (
    build_schema, 
    GraphQLObjectType, 
    GraphQLInputObjectType, 
    GraphQLEnumType, 
    GraphQLScalarType
)

class SimpleGraphQLParser:

    def __init__(self, schema_content):
        self.schema = build_schema(schema_content)
        
        self.definitions = {
            "types": {},
            "inputs": {},
            "enums": {},
            "scalars": set()
        }
        self._extract_definitions()

    def _extract_definitions(self):
        type_map = self.schema.type_map
        
        for name, g_type in type_map.items():
            if name.startswith('__'): 
                continue
            
            # 1. Types (Objekte)
            if isinstance(g_type, GraphQLObjectType):
                # Query/Mutation/Subscription landen auch hier, das ist ok.
                self.definitions["types"][name] = self._convert_fields(g_type.fields)
            
            # 2. Inputs
            elif isinstance(g_type, GraphQLInputObjectType):
                self.definitions["inputs"][name] = self._convert_fields(g_type.fields)
            
            # 3. Enums
            elif isinstance(g_type, GraphQLEnumType):
                # values.keys() gibt die Enum-Namen (z.B. 'Live', 'Test')
                self.definitions["enums"][name] = list(g_type.values.keys())
            
            # 4. Scalars
            elif isinstance(g_type, GraphQLScalarType):
                self.definitions["scalars"].add(name)

    def _convert_fields(self, fields):
        """
        Hilfsfunktion: Wandelt graphql-core Felder in unser einfaches Dict-Format um.
        Format: {'fieldName': {'type': 'String!', 'args': {...}}}
        """
        result = {}
        for fname, fdef in fields.items():
            field_data = {
                "type": str(fdef.type), 
                "args": {}
            }
            
            # Argumente extrahieren (falls vorhanden)
            if hasattr(fdef, 'args'):
                for arg_name, arg_def in fdef.args.items():
                    field_data["args"][arg_name] = {"type": str(arg_def.type)}
            
            result[fname] = field_data
        return result

    def get_query_type(self):
        """Gibt die Felder des Query-Root-Objekts zurück."""
        if self.schema.query_type:
            return self._convert_fields(self.schema.query_type.fields)
        return None

    def get_mutation_type(self):
        """Gibt die Felder des Mutation-Root-Objekts zurück."""
        if self.schema.mutation_type:
            return self._convert_fields(self.schema.mutation_type.fields)
        return None