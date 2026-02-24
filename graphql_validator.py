import json
import os
from jsonschema import validate, ValidationError

class GraphQLSchemaValidator:
    def __init__(self, schema_path):
        """
        Lädt das generierte JSON-Schema.
        """
        if not os.path.exists(schema_path):
            raise FileNotFoundError(f"Schema Datei nicht gefunden: {schema_path}")
            
        with open(schema_path, 'r', encoding='utf-8') as f:
            self.full_schema = json.load(f)
            
        self.definitions = self.full_schema.get("definitions", {})

    def _get_operation_field_schema(self, operation_type, field_name):
        """
        Holt das Schema für ein spezifisches Feld innerhalb von Query oder Mutation.
        z.B. operation_type='Query', field_name='simDetails'
        """
        # Suche nach dem Typ "Query" oder "Mutation" in den Definitionen
        root_op = self.definitions.get(operation_type)
        if not root_op:
            raise ValueError(f"Typ '{operation_type}' nicht im Schema gefunden.")
            
        properties = root_op.get("properties", {})
        field_schema = properties.get(field_name)
        
        if not field_schema:
            raise ValueError(f"Feld '{field_name}' existiert nicht im Typ '{operation_type}'.")
            
        return field_schema

    def validate_response(self, response_data, operation_name, operation_type="Query"):
        """
        Validiert eine komplette GraphQL Response.
        
        Args:
            response_data (dict): Das JSON Dictionary der Antwort (inkl. "data" Key).
            operation_name (str): Der Name der Query/Mutation (z.B. "simDetails").
            operation_type (str): "Query" oder "Mutation".
        """
        
        # 1. Wir holen uns die Referenzdefinition für die gewünschte Query
        target_schema_ref = self._get_operation_field_schema(operation_type, operation_name)
        
        # 2. Wir bauen ein temporäres Schema, das die GraphQL-Struktur abbildet:
        # { "data": { "simDetails": { ... ref ... } } }
        validation_schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "definitions": self.definitions, # Wichtig: Alle Definitionen müssen verfügbar sein
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "properties": {
                        operation_name: target_schema_ref
                    },
                    "required": [operation_name]
                    # "additionalProperties": False # Optional: Falls wir streng sein wollen
                },
                "errors": {
                    "type": "array"
                }
            },
            "required": ["data"]
        }

        # 3. Validierung durchführen
        try:
            validate(instance=response_data, schema=validation_schema)
            return True
        except ValidationError as e:
            print(f"Validierungsfehler bei {operation_name}: {e.message}")
            print(f"Pfad zum Fehler: {list(e.path)}")
            raise e