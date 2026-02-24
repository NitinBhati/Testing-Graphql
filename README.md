# GraphQL API Testing Framework
This project is an automated testing suite for GraphQL APIs using Python.

## Core Components
* **Schema Parser:** Converts `.graphql` files into Python dictionaries.
* **Query Generator:** Automatically creates GraphQL queries and variables.
* **Allure Client:** Executes requests and generates visual reports.
* **Schema Validator:** Ensures API responses match the official schema.

## How to Run
1. Install dependencies: `pip install pytest allure-pytest requests jsonschema graphql-core`
2. Run tests: `pytest test_suite.py`
3. Generate Report: `allure serve allure-results`
