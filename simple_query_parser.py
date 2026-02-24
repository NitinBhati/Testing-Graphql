from graphql import parse, OperationDefinitionNode, FieldNode, VariableDefinitionNode

class SimpleQueryParser:
    """
    Parst Queries mithilfe von graphql-core und extrahiert:
    1. Operation Type (query/mutation)
    2. Selection Set (die angefragten Felder)
    3. Variable Definitions (welche Variablen erwartet werden)
    """
    def parse(self, query_str):
        try:
            document = parse(query_str)
        except Exception as e:
            raise ValueError(f"Query Syntax Fehler: {e}")

        # Wir nehmen die erste Operation im Dokument an
        op_def = None
        for definition in document.definitions:
            if isinstance(definition, OperationDefinitionNode):
                op_def = definition
                break
        
        if not op_def:
            raise ValueError("Keine Operation (Query/Mutation) gefunden.")

        # 1. Selection Set extrahieren (rekursiv)
        selection_tree = self._extract_selection(op_def.selection_set)

        # 2. Variablen Definitionen extrahieren
        # Format: {'varName': 'TypeString'} z.B. {'input': 'SimActivateInput!'}
        variable_defs = {}
        for var_def in op_def.variable_definitions:
            var_name = var_def.variable.name.value
            var_type = self._get_type_string(var_def.type)
            variable_defs[var_name] = var_type

        return {
            "type": op_def.operation.value, # "query" oder "mutation"
            "name": op_def.name.value if op_def.name else None,
            "fields": selection_tree,
            "variables": variable_defs 
        }

    def _extract_selection(self, selection_set):
        if not selection_set:
            return None
        
        fields = {}
        for selection in selection_set.selections:
            if isinstance(selection, FieldNode):
                field_name = selection.name.value
                # Alias handling: Wenn alias existiert, nutzen wir den Key im Result
                # key = selection.alias.value if selection.alias else field_name
                
                # Wir brauchen hier aber den echten Namen im Schema, nicht den Alias
                # (für die Validierung gegen das Schema)
                
                sub_selection = self._extract_selection(selection.selection_set)
                fields[field_name] = sub_selection
                
        return fields

    def _get_type_string(self, type_node):
        """Rekursive Hilfsfunktion um Typen wie [String!]! als String zu bekommen"""
        # Dies ist eine Vereinfachung. graphql-core hat eigene Printer,
        # aber wir bauen es hier manuell für volle Kontrolle.
        
        # 1. NonNull Type
        if hasattr(type_node, 'kind') and type_node.kind == 'non_null_type':
            return f"{self._get_type_string(type_node.type)}!"
        
        # 2. List Type
        if hasattr(type_node, 'kind') and type_node.kind == 'list_type':
            return f"[{self._get_type_string(type_node.type)}]"
        
        # 3. Named Type
        if hasattr(type_node, 'name'):
            return type_node.name.value
            
        return "Unknown"
        