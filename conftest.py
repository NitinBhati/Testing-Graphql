import pytest
import os
from graphql_validator import GraphQLSchemaValidator
from dynamic_validator import DynamicGraphQLValidator
from graphql_client import AllureGraphQLClient
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SCHEMA_FILE = "schema.graphql"

# Configuration matching your karate-config.js
CONFIG = {
    "env": "dev",
    "graphql_base_url": "https://api.deutschetelekom.api/v1/sims/graphql",
    "oauth": {
        "token_url": "https://api.deutschetelekom.api/auth",
        "client_id": "TestClient,
        "client_secret": "clientSecret",
        "api_key": "testAPI",
    }
}

SCHEMA_FILE = "/app/tests/schema.graphql"

@pytest.fixture(scope="session")
def api_context():
    """Returns the base URL and config"""
    return CONFIG

@pytest.fixture(scope="session")
def auth_headers(api_context):
    """
    Equivalent to oauth-token.feature.
    Fetches the token once per test session.
    """
    url = api_context["oauth"]["token_url"]

    # Based on oauth-token.feature: headers are sent to get the token
    headers = {
        "accept": "application/json",
        "clientid": api_context["oauth"]["client_id"],
        "clientsecret": api_context["oauth"]["client_secret"],
        "apikey": api_context["oauth"]["api_key"]
    }

    # Verify SSL is handled (Karate config had ssl=true, requests validates by default)
    # If you need to ignore SSL errors like in dev, verify=False
    response = requests.post(url, headers=headers, verify=False)

    assert response.status_code == 200, f"Auth failed: {response.text}"
    data = response.json()

    # Extract token (Karate: response.IOTToken)
    token = data.get("IOTToken")

    # Return the headers to be used in all GraphQL requests
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "apikey": api_context["oauth"]["api_key"],
        "IOTToken": token
    }

@pytest.fixture(scope="session")
def auth_token(api_context):
    """Retrieves the token once, ignoring SSL errors."""
    url = api_context["oauth"]["token_url"]
    headers = {
        "accept": "application/json",
        "clientid": api_context["oauth"]["client_id"],
        "clientsecret": api_context["oauth"]["client_secret"],
        "apikey": api_context["oauth"]["api_key"]
    }
    
    response = requests.post(url, headers=headers, verify=False)
    assert response.status_code == 200, f"Auth failed: {response.text}"
    
    return response.json().get("IOTToken")

@pytest.fixture(scope="session")
def api_client(api_context, auth_token):
    """
    Returns a configured requests.Session object.
    This session will automatically attach headers and handle SSL settings
    for every test, so you don't have to repeat 'verify=False'.
    """
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json",
        "apikey": api_context["oauth"]["api_key"],
        "IOTToken": auth_token
    })
    session.verify = False
    return session

@pytest.fixture(scope="session")
def validator():
    if not os.path.exists(SCHEMA_FILE):
        pytest.fail(f"Schema Datei {SCHEMA_FILE} fehlt.")
    return DynamicGraphQLValidator(SCHEMA_FILE)

@pytest.fixture
def mock_graphql_response():
    """
    Nur für Demo-Zwecke: Ein Mock für eine API-Antwort.
    In echten Tests würden Sie hier 'requests' oder einen GraphQL Client nutzen.
    """
    def _factory(query_name, data_payload):
        return {
            "data": {
                query_name: data_payload
            }
        }
    return _factory

@pytest.fixture(scope="session")
def client(api_context, auth_token):
    """
    Stellt den AllureGraphQLClient bereit.
    """
    return AllureGraphQLClient(api_context, auth_token)