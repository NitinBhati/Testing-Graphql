import allure
import pytest
from generated_queries_v2 import QUERIES, MUTATIONS
from jsonschema import ValidationError
import copy

@allure.feature("simChangeStatus")
@allure.story("Check Schema for simChangeStatus")
@allure.severity(allure.severity_level.CRITICAL)

def test_simChangeStatus(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "simChangeStatus"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
        
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("simLastSessionDetails")
@allure.story("Check Schema for simLastSessionDetails")
@allure.severity(allure.severity_level.CRITICAL)

def test_simLastSessionDetails(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "simLastSessionDetails"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
        
        variables["imsi"]="262199099000031"
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("customer")
@allure.story("Check Schema for customer")
@allure.severity(allure.severity_level.NORMAL)

def test_customer(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "customer"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]

    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("accountBalance")
@allure.story("Check Schema for accountBalance")
@allure.severity(allure.severity_level.MINOR)

def test_accountBalance(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "accountBalance"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]

    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("agreementId")
@allure.story("Check Schema for agreementId")
@allure.severity(allure.severity_level.MINOR)

def test_agreementsId(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "agreementsId"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]

    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("businessUnit")
@allure.story("Check Schema for businessUnit")
@allure.severity(allure.severity_level.MINOR)

def test_businessUnit(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "businessUnit"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
        #overwrite variables:
        variables = {"input":{"businessUnitId": "Bf0HAwAAAYf3hu_XmvK9gNrCAAE"}}
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("simOrderState")
@allure.story("Check Schema for simOrderState")
@allure.severity(allure.severity_level.CRITICAL)

def test_simOrderState(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "simOrderState"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
        variables["id"] = "MvoLBBzZDBJHxvoBbslfsTKFkKc"
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("simModuleList")
@allure.story("Check Schema for simModuleList")
@allure.severity(allure.severity_level.NORMAL)

def test_simModuleList(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "simModuleList"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("downloadInvoice")
@allure.story("Check Schema for downloadInvoice")
@allure.severity(allure.severity_level.MINOR)

def test_downloadInvoice(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "downloadInvoice"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
        variables = {
            "input": {
                "invoiceId": "cd8ce2db0eb14244b09097c69c80a544"
            }
        }
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("apnProfiles")
@allure.story("Check Schema for apnProfiles")
@allure.severity(allure.severity_level.NORMAL)

def test_apnProfiles(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "apnProfiles"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
        variables["customerId"] = "MvoHAwAAAYbMS5nIHpGBKb9lAAE"
        del variables["apnType"]
        del variables["allocationType"]
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("simDetails")
@allure.story("Check Schema for simDetails")
@allure.severity(allure.severity_level.CRITICAL)

def test_simDetails(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "simDetails"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
        variables["imsi"]="262199099000031"
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("simList")
@allure.story("Check Schema for simList")
@allure.severity(allure.severity_level.CRITICAL)

def test_simList(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "simList"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("serviceProfileList")
@allure.story("Check Schema for serviceProfileList")
@allure.severity(allure.severity_level.NORMAL)

def test_serviceProfileList(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "serviceProfileList"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("simChangeList")
@allure.story("Check Schema for simChangeList")
@allure.severity(allure.severity_level.CRITICAL)

def test_simChangeList(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "simChangeList"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("simSessionHistory")
@allure.story("Check Schema for simSessionHistory")
@allure.severity(allure.severity_level.CRITICAL)

def test_simSessionHistory(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "simSessionHistory"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
        variables["input"]["imsi"]="262199099000031"
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("costCentersList")
@allure.story("Check Schema for costCentersList")
@allure.severity(allure.severity_level.MINOR)

def test_costCentersList(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "costCentersList"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("businessUnitsList")
@allure.story("Check Schema for businessUntisList")
@allure.severity(allure.severity_level.MINOR)

def test_businessUnitsList(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "businessUnitsList"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("monitoringProfiles")
@allure.story("Check Schema for monitoringProfiles")
@allure.severity(allure.severity_level.NORMAL)

def test_monitoringProfiles(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "monitoringProfiles"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("simCustomAttributeSets")
@allure.story("Check Schema for simCustomerAttributeSets")
@allure.severity(allure.severity_level.NORMAL)

def test_simCustomAttributeSets(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "simCustomAttributeSets"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("simOrderList")
@allure.story("Check Schema for simOrderList")
@allure.severity(allure.severity_level.CRITICAL)

def test_simOrderList(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "simOrderList"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)
    
@allure.feature("invoiceList")
@allure.story("Check Schema for invoiceList")
@allure.severity(allure.severity_level.NORMAL)

def test_invoiceList(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "invoiceList"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("systemVersion")
@allure.story("Check Schema for currentUser")
@allure.severity(allure.severity_level.MINOR)

def test_systemVersion(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "systemVersion"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
    
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)

@allure.feature("currentUser")
@allure.story("Check Schema for currentUser")
@allure.severity(allure.severity_level.MINOR)

def test_currentUser(validator, client):
    with allure.step("Vorbereitung der Query"):
        op_name = "currentUser"
        op_data = QUERIES[op_name]
        
        query_str = op_data["query"]
        variables = op_data["variables"]
        
        #replace query_string
        query_str = "query CurrentUserTest($filter: MutationsAccessFilterInput, $filter1: QueriesAccessFilterInput, $filter2: FieldsAccessFilterInput) {\n  currentUser {\n    vendorId\n    vendorNamedId\n    username\n    userId\n    appId\n    email\n    accessCtx\n    privacyLevel\n    privileges\n    readOnly\n    enabledFeatures\n    enabledApps\n    mutationsAccess(filter: $filter) {\n      parentType\n      fieldName\n      exists\n      hasAccess\n      grantedRoles\n      requiredRoles\n    }\n    queriesAccess(filter: $filter1) {\n      parentType\n      fieldName\n      exists\n      hasAccess\n      grantedRoles\n      requiredRoles\n    }\n    unreadGuiNotificationCount\n  }\n}"
    response = client.execute(query_str,variables)

    with allure.step("Validierung gegen Schema"):
        validator.validate(query_str, response, variables=variables)
