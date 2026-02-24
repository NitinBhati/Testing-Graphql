import requests
import json
import allure
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class AllureGraphQLClient:
    def __init__(self, api_context, auth_token):
        self.base_url = api_context["graphql_base_url"]
        # Optional: Headers (z.B. Auth) hier setzen
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "apikey": api_context["oauth"]["api_key"],
            "IOTToken": auth_token
        }

    def execute(self, query, variables=None, operation_name=None):
        """
        Führt einen GraphQL Request aus und protokolliert alles in Allure.
        """
        payload = {"query": query}
        if variables:
            payload["variables"] = variables
        if operation_name:
            payload["operationName"] = operation_name

        # 1. Query & Variablen VOR dem Request anhängen (falls Timeout/Crash)
        self._attach_request(query, variables)

        try:
            response = requests.post(self.base_url, json=payload, headers=self.headers, timeout=10, verify=False)
            try:
                response_data = response.json()
            except ValueError:
                response_data = {"error": "Invalid JSON", "text": response.text}
            status_code = response.status_code

            # 3. Response NACH dem Request anhängen
            self._attach_response(status_code, response_data)

            # Fehler werfen, wenn HTTP Status nicht 200 ist (optional)
            if status_code != 200:
                raise Exception(f"API Fehler {status_code}: {response_data}")

            return response_data

        except Exception as e:
            # Auch bei Python-Exceptions (z.B. ConnectionError) wollen wir das loggen
            allure.attach(str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
            raise e

    def _attach_request(self, query, variables):
        """Hilfsfunktion für Allure Attachments"""
        with allure.step("GraphQL Request senden"):
            allure.attach(query, name="Query", attachment_type=allure.attachment_type.TEXT)
            if variables:
                allure.attach(
                    json.dumps(variables, indent=2), 
                    name="Variables", 
                    attachment_type=allure.attachment_type.JSON
                )

    def _attach_response(self, status_code, body):
        """Hilfsfunktion für Response Attachments"""
        with allure.step(f"Response erhalten (Status: {status_code})"):
            allure.attach(
                json.dumps(body, indent=2), 
                name="Response Body", 
                attachment_type=allure.attachment_type.JSON
            )
            