DEFAULTS = {
    "SCALARS": {
        "IMSI": "262199099999999",
        "ICCID": None,
        "String": "test_string",
        "Boolean": False,
        "Int": 0,
        "ID": "ID_PLACEHOLDER",
        "SimChangeId": "E1ELAqpIEDJbtz"
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
            "imsi": "262199099999999999",
            "iccid": None
        },
        "BusinessUnitDetailsParametersInput": {
            "input": {
                "businessUnitId": "Bf0HAwAAAYf3h"
            }
        },
        "InvoiceDownloadParametersInput": {
            "input": {
                "invoiceId": "cd8ce2db0eb14244b090"
            }
        }
    }
}

QUERIES = {
    "simChangeStatus": {
        "query": "query simChangeStatus($simChangeId: SimChangeId!) {\n  simChangeStatus(simChangeId: $simChangeId) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "simChangeId": "E1ELAqpIEDJbtz"
        }
    },
    "simLastSessionDetails": {
        "query": "query simLastSessionDetails($imsi: IMSI, $iccid: ICCID) {\n  simLastSessionDetails(imsi: $imsi, iccid: $iccid) {\n    startTime\n    endTime\n    updateTime\n    location {\n    mcc\n    mnc\n    lac\n    cell\n  }\n    upLink\n    downLink\n    ipAddressV4\n    ipAddressV6Prefix\n    imei\n    imeiInfo {\n    baseImei\n    imei\n    imeisv\n    checkDigit\n    softwareVersionDigit\n    expectedDigit\n    isValid\n    typeApprovalCode\n    serialNumber\n  }\n  }\n}",
        "variables": {
            "imsi": None,
            "iccid": None
        }
    },
    "customer": {
        "query": "query customer {\n  customer {\n    id\n    name\n    organizationType\n    businessSegment\n    address {\n    addressLines\n    postalCode\n    city\n    countryName\n  }\n    deliveryAddress {\n    addressLines\n    postalCode\n    city\n    countryName\n  }\n    billingAddress {\n    addressLines\n    postalCode\n    city\n    countryName\n  }\n    legalIds {\n    idType\n    value\n  }\n    contactData {\n    email\n    phone\n  }\n    accountManager {\n    id\n    name\n    position\n    contact {\n    email\n    mobile\n    phone\n  }\n  }\n  }\n}",
        "variables": {}
    },
    "accountBalance": {
        "query": "query accountBalance {\n  accountBalance {\n    balance\n  }\n}",
        "variables": {}
    },
    "agreementsId": {
        "query": "query agreementsId {\n  agreementsId {\n    edges {\n    id\n  }\n  }\n}",
        "variables": {}
    },
    "businessUnit": {
        "query": "query businessUnit($input: BusinessUnitDetailsParametersInput!) {\n  businessUnit(input: $input) {\n    id\n    name\n    organizationType\n    businessSegment\n    address {\n    addressLines\n    postalCode\n    city\n    countryName\n  }\n    deliveryAddress {\n    addressLines\n    postalCode\n    city\n    countryName\n  }\n    billingAddress {\n    addressLines\n    postalCode\n    city\n    countryName\n  }\n    legalIds {\n    idType\n    value\n  }\n    contactData {\n    email\n    phone\n  }\n    accountManager {\n    id\n    name\n    position\n    contact {\n    email\n    mobile\n    phone\n  }\n  }\n  }\n}",
        "variables": {
            "input": {
                "input": {
                    "businessUnitId": "Bf0HAwAAAYf3h"
                }
            }
        }
    },
    "simOrderState": {
        "query": "query simOrderState($id: String!) {\n  simOrderState(id: $id) {\n    state\n    prettyId\n  }\n}",
        "variables": {
            "id": "test_string"
        }
    },
    "simModuleList": {
        "query": "query simModuleList($input: SimModuleParametersInput) {\n  simModuleList(input: $input) {\n    pageInfo {\n    totalRelation\n    size\n    hasNextPage\n    hasPreviousPage\n    startCursor\n    startPosition\n    endCursor\n    endPosition\n  }\n    edges {\n    node {\n    id\n    name\n    packageSizes\n  }\n    cursor\n    cursorPosition\n  }\n  }\n}",
        "variables": {
            "input": {
                "pageInfo": {
                    "first": 10,
                    "after": None,
                    "before": None,
                    "last": None,
                    "limit": None,
                    "offset": 0
                }
            }
        }
    },
    "downloadInvoice": {
        "query": "query downloadInvoice($input: InvoiceDownloadParametersInput!) {\n  downloadInvoice(input: $input) {\n    url\n  }\n}",
        "variables": {
            "input": {
                "invoiceId": "cd8ce2db0eb14244b090"
            }
        }
    },
    "apnProfiles": {
        "query": "query apnProfiles($customerId: String!, $apnName: String, $apnType: ApnType, $activationDateFrom: OffsetDateTime, $activationDateTo: OffsetDateTime, $allocationType: AllocationType) {\n  apnProfiles(customerId: $customerId, apnName: $apnName, apnType: $apnType, activationDateFrom: $activationDateFrom, activationDateTo: $activationDateTo, allocationType: $allocationType) {\n    pageInfo {\n    totalRelation\n    size\n    hasNextPage\n    hasPreviousPage\n    startCursor\n    startPosition\n    endCursor\n    endPosition\n  }\n    edges {\n    node {\n    id\n    customerId\n    name\n    state\n    activationDate\n    apnType\n  }\n    cursor\n    cursorPosition\n  }\n  }\n}",
        "variables": {
            "customerId": "test_string",
            "apnName": None,
            "apnType": None,
            "activationDateFrom": None,
            "activationDateTo": None,
            "allocationType": None
        }
    },
    "simDetails": {
        "query": "query simDetails($imsi: IMSI, $iccid: ICCID) {\n  simDetails(imsi: $imsi, iccid: $iccid) {\n    imsi\n    msisdn\n    iccid\n    imei\n    caption\n    labels\n    customer {\n    id\n    name\n  }\n    usageProfile {\n    currentState\n    dataLimits {\n    name\n  }\n    voiceLimits {\n    name\n  }\n    smsLimits {\n    name\n  }\n  }\n    customAttributes {\n    configId\n    tags\n    f01\n    f02\n    f03\n    f04\n    f05\n    f06\n    f07\n    f08\n    f09\n    f10\n  }\n    businessUnit {\n    id\n    name\n  }\n    simSettings {\n    dataService\n    smsMoService\n    smsMtService\n    voiceIncomingService\n    voiceOutgoingService\n  }\n    status\n    apns {\n    apnName\n    allocationType\n    staticIPv4Addresses\n    staticIPv6Addresses\n    isDefault\n  }\n    networkSlices {\n    snssai {\n    serviceType\n    serviceDifferentiator\n    serviceTypeNum\n  }\n    isDefault\n    defaultDnnName\n  }\n    activationDate\n    usageAllowances {\n    name\n    service\n    bundleType\n    volume {\n    dataBytes\n    dataDuration\n    dataSessions\n    smsCalls\n    voiceCalls\n    voiceDuration\n  }\n    volumePrice\n  }\n    availableSharedAllowances {\n    grantedAllowanceId\n    name\n  }\n    availableNonSharedAllowances {\n    name\n    subscriptionId\n  }\n    pin1\n    pin2\n    puk1\n    puk2\n    eProfile {\n    eid\n    smSrId\n    state\n    roles\n    smDpAddress\n    matchingId\n    activationCode {\n    value\n    qrValue\n  }\n  }\n    roamingSettings {\n    dataRoaming\n    smsMoRoaming\n    voiceRoaming\n  }\n    usageInformation {\n    data {\n    upLink\n    downLink\n  }\n  }\n    installLocation {\n    addressLines\n    postalCode\n    city\n    adminUnits\n    countryIso\n  }\n    lastSessionDetails {\n    startTime\n    endTime\n    updateTime\n    location {\n    mcc\n    mnc\n    lac\n    cell\n  }\n    upLink\n    downLink\n    ipAddressV4\n    ipAddressV6Prefix\n    imei\n    imeiInfo {\n    baseImei\n    imei\n    imeisv\n    checkDigit\n    softwareVersionDigit\n    expectedDigit\n    isValid\n    typeApprovalCode\n    serialNumber\n  }\n  }\n    allowances {\n    pageInfo {\n    totalRelation\n    size\n    hasNextPage\n    hasPreviousPage\n    startCursor\n    startPosition\n    endCursor\n    endPosition\n  }\n    edges {\n    node { __typename }\n    cursor\n    cursorPosition\n  }\n  }\n    imeiInfo {\n    baseImei\n    imei\n    imeisv\n    checkDigit\n    softwareVersionDigit\n    expectedDigit\n    isValid\n    typeApprovalCode\n    serialNumber\n  }\n  }\n}",
        "variables": {
            "imsi": None,
            "iccid": None
        }
    },
    "simList": {
        "query": "query simList($input: SimListParametersInput) {\n  simList(input: $input) {\n    pageInfo {\n    totalRelation\n    size\n    hasNextPage\n    hasPreviousPage\n    startCursor\n    startPosition\n    endCursor\n    endPosition\n  }\n    edges {\n    node {\n    imsi\n    msisdn\n    iccid\n    imei\n    caption\n    labels\n    status\n    activationDate\n    pin1\n    pin2\n    puk1\n    puk2\n  }\n    cursor\n    cursorPosition\n  }\n  }\n}",
        "variables": {
            "input": {
                "pageInfo": {
                    "first": 10,
                    "after": None,
                    "before": None,
                    "last": None,
                    "limit": None,
                    "offset": 0
                },
                "serviceProfileId": None,
                "simStatus": [],
                "label": None,
                "since": None,
                "imsis": [],
                "iccids": [],
                "orderId": None,
                "sortBy": None
            }
        }
    },
    "serviceProfileList": {
        "query": "query serviceProfileList($input: ServiceProfileListParametersInput) {\n  serviceProfileList(input: $input) {\n    pageInfo {\n    totalRelation\n    size\n    hasNextPage\n    hasPreviousPage\n    startCursor\n    startPosition\n    endCursor\n    endPosition\n  }\n    edges {\n    node {\n    id\n    name\n  }\n    cursor\n    cursorPosition\n  }\n  }\n}",
        "variables": {
            "input": {
                "paging": {
                    "first": 10,
                    "after": None,
                    "before": None,
                    "last": None,
                    "limit": None,
                    "offset": 0
                },
                "sortBy": None
            }
        }
    },
    "simChangeList": {
        "query": "query simChangeList($input: SimChangeListParametersInput) {\n  simChangeList(input: $input) {\n    pageInfo {\n    totalRelation\n    size\n    hasNextPage\n    hasPreviousPage\n    startCursor\n    startPosition\n    endCursor\n    endPosition\n  }\n    edges {\n    node {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n    cursor\n    cursorPosition\n  }\n  }\n}",
        "variables": {
            "input": {
                "paging": {
                    "first": 10,
                    "after": None,
                    "before": None,
                    "last": None,
                    "limit": None,
                    "offset": 0
                },
                "imsi": None,
                "iccid": None,
                "sortBy": None
            }
        }
    },
    "simSessionHistory": {
        "query": "query simSessionHistory($input: SessionHistoryParametersInput!) {\n  simSessionHistory(input: $input) {\n    pageInfo {\n    totalRelation\n    size\n    hasNextPage\n    hasPreviousPage\n    startCursor\n    startPosition\n    endCursor\n    endPosition\n  }\n    edges {\n    node {\n    sessionId\n    state\n    ggsnIpAddress\n    sgsnAddress\n    sessionStartTime\n    sessionEndTime\n    updateTime\n    apnName\n    upLink\n    downLink\n    ipAddressV4\n    ipAddressV6Prefix\n    imei\n    usage\n    serviceType\n    technologyType\n    subscriptionName\n    msisdn\n    iccid\n    duration\n    terminationReason\n  }\n    cursor\n    cursorPosition\n  }\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "paging": {
                    "first": 10,
                    "after": None,
                    "before": None,
                    "last": None,
                    "limit": None,
                    "offset": 0
                },
                "timeFrame": None,
                "sortBy": None,
                "filter": {
                    "serviceTypes": [
                        "Data"
                    ]
                }
            }
        }
    },
    "costCentersList": {
        "query": "query costCentersList($input: CostCentersParametersInput) {\n  costCentersList(input: $input) {\n    pageInfo {\n    totalRelation\n    size\n    hasNextPage\n    hasPreviousPage\n    startCursor\n    startPosition\n    endCursor\n    endPosition\n  }\n    edges {\n    node {\n    id\n    name\n  }\n    cursor\n    cursorPosition\n  }\n  }\n}",
        "variables": {
            "input": {
                "pageInfo": {
                    "first": 10,
                    "after": None,
                    "before": None,
                    "last": None,
                    "limit": None,
                    "offset": 0
                },
                "sortBy": None
            }
        }
    },
    "businessUnitsList": {
        "query": "query businessUnitsList($input: BusinessUnitsParametersInput) {\n  businessUnitsList(input: $input) {\n    pageInfo {\n    totalRelation\n    size\n    hasNextPage\n    hasPreviousPage\n    startCursor\n    startPosition\n    endCursor\n    endPosition\n  }\n    edges {\n    node {\n    id\n    name\n  }\n    cursor\n    cursorPosition\n  }\n  }\n}",
        "variables": {
            "input": {
                "pageInfo": {
                    "first": 10,
                    "after": None,
                    "before": None,
                    "last": None,
                    "limit": None,
                    "offset": 0
                },
                "sortBy": None
            }
        }
    },
    "monitoringProfiles": {
        "query": "query monitoringProfiles($input: UsageProfilesParametersInput!) {\n  monitoringProfiles(input: $input) {\n    pageInfo {\n    totalRelation\n    size\n    hasNextPage\n    hasPreviousPage\n    startCursor\n    startPosition\n    endCursor\n    endPosition\n  }\n    edges {\n    node {\n    id\n    name\n  }\n    cursor\n    cursorPosition\n  }\n  }\n}",
        "variables": {
            "input": {
                "pageInfo": {
                    "first": 10,
                    "after": None,
                    "before": None,
                    "last": None,
                    "limit": None,
                    "offset": 0
                },
                "customerId": "test_string",
                "sortBy": None
            }
        }
    },
    "simCustomAttributeSets": {
        "query": "query simCustomAttributeSets($input: CustomAttrQueryInputInput) {\n  simCustomAttributeSets(input: $input) {\n    pageInfo {\n    totalRelation\n    size\n    hasNextPage\n    hasPreviousPage\n    startCursor\n    startPosition\n    endCursor\n    endPosition\n  }\n    edges {\n    node {\n    id\n    name\n  }\n    cursor\n    cursorPosition\n  }\n  }\n}",
        "variables": {
            "input": {
                "pageInfo": {
                    "first": 10,
                    "after": None,
                    "before": None,
                    "last": None,
                    "limit": None,
                    "offset": 0
                },
                "sortBy": None
            }
        }
    },
    "simOrderList": {
        "query": "query simOrderList($input: SimProfileOrderParametersInput) {\n  simOrderList(input: $input) {\n    pageInfo {\n    totalRelation\n    size\n    hasNextPage\n    hasPreviousPage\n    startCursor\n    startPosition\n    endCursor\n    endPosition\n  }\n    edges {\n    node {\n    id\n    prettyId\n    agreementId\n    businessUnit\n    createdForBusinessUnit\n    orderAlias\n    createdAt\n    completedAt\n    status\n    trackingNumber\n  }\n    cursor\n    cursorPosition\n  }\n  }\n}",
        "variables": {
            "input": {
                "pageInfo": {
                    "first": 10,
                    "after": None,
                    "before": None,
                    "last": None,
                    "limit": None,
                    "offset": 0
                },
                "sortBy": None
            }
        }
    },
    "invoiceList": {
        "query": "query invoiceList($input: InvoiceInfoParametersInput) {\n  invoiceList(input: $input) {\n    pageInfo {\n    totalRelation\n    size\n    hasNextPage\n    hasPreviousPage\n    startCursor\n    startPosition\n    endCursor\n    endPosition\n  }\n    edges {\n    node {\n    id\n  }\n    cursor\n    cursorPosition\n  }\n  }\n}",
        "variables": {
            "input": {
                "pageInfo": {
                    "first": 10,
                    "after": None,
                    "before": None,
                    "last": None,
                    "limit": None,
                    "offset": 0
                },
                "sortBy": None
            }
        }
    },
    "systemVersion": {
        "query": "query systemVersion {\n  systemVersion {\n    appName\n    version\n    buildVersion\n    buildDate\n    gitHeadRev\n    gitCommitDate\n    gitBranch\n    envName\n    envType\n    envFeatures\n  }\n}",
        "variables": {}
    },
    "currentUser": {
        "query": "query currentUser {\n  currentUser {\n    vendorId\n    vendorNamedId\n    username\n    userId\n    appId\n    email\n    accessCtx\n    privacyLevel\n    privileges\n    readOnly\n    enabledFeatures\n    enabledApps\n    unreadGuiNotificationCount\n    authenticationPolicy {\n    internalRealm {\n    otpConfigRequirement\n    loginConfigEmailAsUsername\n    internalRegistrationEnabled\n    registrationConfigExternalUsers\n  }\n    externalRealm {\n    otpConfigRequirement\n    loginConfigEmailAsUsername\n    internalRegistrationEnabled\n    registrationConfigExternalUsers\n  }\n  }\n  }\n}",
        "variables": {}
    }
}

MUTATIONS = {
    "simRemoveMonitoringProfile": {
        "query": "mutation simRemoveMonitoringProfile($input: UnassignMonitoringProfileInputInput!) {\n  simRemoveMonitoringProfile(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None
            }
        }
    },
    "simConfigureApns": {
        "query": "mutation simConfigureApns($input: SimConfigureApnsInput!) {\n  simConfigureApns(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "networkSettings": [
                    {
                        "apnName": "test_string",
                        "allocationType": None,
                        "staticIPv4Address": None,
                        "staticIPv6Address": None,
                        "staticIPv4Addresses": [],
                        "staticIPv6Addresses": [],
                        "deviceAuth": None,
                        "isDefault": None
                    }
                ],
                "networkSlices": [
                    {
                        "snssai": {
                            "serviceType": "eMBB",
                            "serviceDifferentiator": None,
                            "serviceTypeNum": None
                        },
                        "defaultDnnName": None
                    }
                ]
            }
        }
    },
    "simAddLabels": {
        "query": "mutation simAddLabels($input: SimLabelsInput!) {\n  simAddLabels(input: $input) {\n    imsi\n    labels\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "label": [
                    "test_string"
                ]
            }
        }
    },
    "simRemoveLabels": {
        "query": "mutation simRemoveLabels($input: SimLabelsInput!) {\n  simRemoveLabels(input: $input) {\n    imsi\n    labels\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "label": [
                    "test_string"
                ]
            }
        }
    },
    "simClearLabels": {
        "query": "mutation simClearLabels($imsi: IMSI, $iccid: ICCID) {\n  simClearLabels(imsi: $imsi, iccid: $iccid) {\n    imsi\n    labels\n  }\n}",
        "variables": {
            "imsi": None,
            "iccid": None
        }
    },
    "simAssignCaption": {
        "query": "mutation simAssignCaption($input: SimAssignCaptionInput!) {\n  simAssignCaption(input: $input) {\n    imsi\n    caption\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "caption": "test_string"
            }
        }
    },
    "simRemoveCaption": {
        "query": "mutation simRemoveCaption($imsi: IMSI, $iccid: ICCID) {\n  simRemoveCaption(imsi: $imsi, iccid: $iccid) {\n    imsi\n    caption\n  }\n}",
        "variables": {
            "imsi": None,
            "iccid": None
        }
    },
    "simFinishSleep": {
        "query": "mutation simFinishSleep($input: SimFinishSleepInputInput!) {\n  simFinishSleep(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "connectivityPlanId": None
            }
        }
    },
    "simChangeServiceProfile": {
        "query": "mutation simChangeServiceProfile($input: SimChangeServiceProfileInput!) {\n  simChangeServiceProfile(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "serviceProfileId": None,
                "connectivityPlanId": None,
                "expectedState": None
            }
        }
    },
    "simConfigureExpectedImei": {
        "query": "mutation simConfigureExpectedImei($input: SimConfigureExpectedImeiInput!) {\n  simConfigureExpectedImei(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "imei": None,
                "imeiLock": False
            }
        }
    },
    "simSendToSleep": {
        "query": "mutation simSendToSleep($input: SimModifyStateInput!) {\n  simSendToSleep(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "serviceProfileId": None,
                "connectivityPlanId": None
            }
        }
    },
    "simMoveToInventory": {
        "query": "mutation simMoveToInventory($input: SimModifyStateInput!) {\n  simMoveToInventory(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "serviceProfileId": None,
                "connectivityPlanId": None
            }
        }
    },
    "simFinishTests": {
        "query": "mutation simFinishTests($input: SimFinishTestsInput!) {\n  simFinishTests(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "stage": None,
                "serviceProfileId": None,
                "connectivityPlanId": None
            }
        }
    },
    "simActivate": {
        "query": "mutation simActivate($input: SimActivateInput!) {\n  simActivate(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "serviceProfileId": None,
                "connectivityPlanId": None,
                "state": None,
                "roamingProfileId": None,
                "sharedAllowanceId": [],
                "nonSharedAllowanceConfig": [
                    {
                        "subscriptionId": "test_string"
                    }
                ],
                "networkSettings": [
                    {
                        "apnName": "test_string",
                        "allocationType": None,
                        "staticIPv4Address": None,
                        "staticIPv6Address": None,
                        "staticIPv4Addresses": [],
                        "staticIPv6Addresses": [],
                        "deviceAuth": None,
                        "isDefault": None
                    }
                ],
                "networkSlices": [
                    {
                        "snssai": {
                            "serviceType": "eMBB",
                            "serviceDifferentiator": None,
                            "serviceTypeNum": None
                        },
                        "defaultDnnName": None
                    }
                ]
            }
        }
    },
    "simTransferToBusinessUnit": {
        "query": "mutation simTransferToBusinessUnit($input: SimTransferToBusinessUnitInput!) {\n  simTransferToBusinessUnit(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "targetUnitId": None,
                "newServiceProfileId": None,
                "newConnectivityPlanId": None,
                "expectedState": None,
                "networkSettings": [
                    {
                        "apnName": "test_string",
                        "allocationType": None,
                        "staticIPv4Address": None,
                        "staticIPv6Address": None,
                        "staticIPv4Addresses": [],
                        "staticIPv6Addresses": [],
                        "deviceAuth": None,
                        "isDefault": None
                    }
                ],
                "networkSlices": [
                    {
                        "snssai": {
                            "serviceType": "eMBB",
                            "serviceDifferentiator": None,
                            "serviceTypeNum": None
                        },
                        "defaultDnnName": None
                    }
                ]
            }
        }
    },
    "simTransferInactiveToBusinessUnit": {
        "query": "mutation simTransferInactiveToBusinessUnit($input: SimTransferInactiveToBusinessUnitInput!) {\n  simTransferInactiveToBusinessUnit(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "targetUnitId": None
            }
        }
    },
    "simChangeCustomAttributes": {
        "query": "mutation simChangeCustomAttributes($input: SimChangeCustomAttrInputInput!) {\n  simChangeCustomAttributes(input: $input) {\n    imsi\n    customAttr {\n    configId\n    tags\n    f01\n    f02\n    f03\n    f04\n    f05\n    f06\n    f07\n    f08\n    f09\n    f10\n  }\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "configId": None,
                "tags": {
                    "clear": None,
                    "remove": [],
                    "add": []
                },
                "f01": {
                    "clear": None,
                    "remove": [],
                    "add": []
                },
                "f02": {
                    "clear": None,
                    "remove": [],
                    "add": []
                },
                "f03": {
                    "clear": None,
                    "remove": [],
                    "add": []
                },
                "f04": {
                    "clear": None,
                    "remove": [],
                    "add": []
                },
                "f05": {
                    "clear": None,
                    "remove": [],
                    "add": []
                },
                "f06": {
                    "clear": None,
                    "remove": [],
                    "add": []
                },
                "f07": {
                    "clear": None,
                    "remove": [],
                    "add": []
                },
                "f08": {
                    "clear": None,
                    "remove": [],
                    "add": []
                },
                "f09": {
                    "clear": None,
                    "remove": [],
                    "add": []
                },
                "f10": {
                    "clear": None,
                    "remove": [],
                    "add": []
                },
                "clearValues": None
            }
        }
    },
    "simAddAllowances": {
        "query": "mutation simAddAllowances($input: SimAllowanceInputInput!) {\n  simAddAllowances(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "shared": [],
                "nonShared": [
                    {
                        "subscriptionId": "test_string"
                    }
                ],
                "validFrom": None
            }
        }
    },
    "simRemoveAllowances": {
        "query": "mutation simRemoveAllowances($input: SimRemoveAllowanceInputInput!) {\n  simRemoveAllowances(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "shared": [],
                "nonShared": []
            }
        }
    },
    "simRemoveRestrictions": {
        "query": "mutation simRemoveRestrictions($input: SimRestrictionsInput!) {\n  simRemoveRestrictions(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "restrictions": [
                    "LostSim"
                ]
            }
        }
    },
    "simApplyRestrictions": {
        "query": "mutation simApplyRestrictions($input: SimRestrictionsInput!) {\n  simApplyRestrictions(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "restrictions": [
                    "LostSim"
                ]
            }
        }
    },
    "simInstallationAddress": {
        "query": "mutation simInstallationAddress($input: SimProfileLocationInputInput!) {\n  simInstallationAddress(input: $input) {\n    imsi\n    installLocation {\n    addressLines\n    postalCode\n    city\n    adminUnits\n    countryIso\n  }\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "installLocation": {
                    "addressLines": [
                        "test_string"
                    ],
                    "postalCode": "test_string",
                    "city": "test_string",
                    "adminUnits": [],
                    "countryIso": "TW"
                }
            }
        }
    },
    "simAssignToCostCenter": {
        "query": "mutation simAssignToCostCenter($input: SimProfileCostCenterInputInput!) {\n  simAssignToCostCenter(input: $input) {\n    imsi\n    costCenterId\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "costCenterId": "test_string"
            }
        }
    },
    "simUpdateAssignedApns": {
        "query": "mutation simUpdateAssignedApns($input: SimUpdateAssignedApnsInput!) {\n  simUpdateAssignedApns(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "networkSettings": [
                    {
                        "apnName": "test_string",
                        "allocationType": None,
                        "staticIPv4Address": None,
                        "staticIPv6Address": None,
                        "staticIPv4Addresses": [],
                        "staticIPv6Addresses": [],
                        "deviceAuth": None,
                        "isDefault": None
                    }
                ]
            }
        }
    },
    "simAssignApns": {
        "query": "mutation simAssignApns($input: SimConfigureApnsInput!) {\n  simAssignApns(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "networkSettings": [
                    {
                        "apnName": "test_string",
                        "allocationType": None,
                        "staticIPv4Address": None,
                        "staticIPv6Address": None,
                        "staticIPv4Addresses": [],
                        "staticIPv6Addresses": [],
                        "deviceAuth": None,
                        "isDefault": None
                    }
                ],
                "networkSlices": [
                    {
                        "snssai": {
                            "serviceType": "eMBB",
                            "serviceDifferentiator": None,
                            "serviceTypeNum": None
                        },
                        "defaultDnnName": None
                    }
                ]
            }
        }
    },
    "simUnassignApns": {
        "query": "mutation simUnassignApns($input: SimUnassignApnsInput!) {\n  simUnassignApns(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "apnNames": [
                    "test_string"
                ],
                "defaultApnName": None,
                "defaultApnsReplacement": [
                    {
                        "apnToReplace": "test_string",
                        "replaceWithApn": None
                    }
                ]
            }
        }
    },
    "simChangeApnsAuth": {
        "query": "mutation simChangeApnsAuth($input: SimChangeApnsAuthSettingsInput!) {\n  simChangeApnsAuth(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "authSettings": None,
                "apnsAuthSettings": [
                    {
                        "apnName": "test_string",
                        "deviceAuth": {
                            "username": None,
                            "password": None
                        }
                    }
                ]
            }
        }
    },
    "simChangeApnsIpSettings": {
        "query": "mutation simChangeApnsIpSettings($input: SimChangeApnsAccessSettingsInput!) {\n  simChangeApnsIpSettings(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "apnsAccessSettings": [
                    {
                        "apnName": "test_string",
                        "allocationType": "Dynamic",
                        "staticIPv4Address": None,
                        "staticIPv6Address": None,
                        "staticIPv4Addresses": [],
                        "staticIPv6Addresses": []
                    }
                ]
            }
        }
    },
    "simTerminate": {
        "query": "mutation simTerminate($input: SimTerminationInput!) {\n  simTerminate(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None
            }
        }
    },
    "simReset": {
        "query": "mutation simReset($input: SimInput!) {\n  simReset(input: $input) {\n    id\n    simId\n    completedTime\n    status\n  }\n}",
        "variables": {
            "input": {
                "imsi": "262199099999999999",
                "iccid": None
            }
        }
    },
    "simReplace": {
        "query": "mutation simReplace($input: SimReplaceInput!) {\n  simReplace(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "targetImsi": None,
                "targetIccid": None
            }
        }
    },
    "simAssignMonitoringProfile": {
        "query": "mutation simAssignMonitoringProfile($input: AssignMonitoringProfileInputInput!) {\n  simAssignMonitoringProfile(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "monitoringProfileId": None
            }
        }
    },
    "simFinishInventory": {
        "query": "mutation simFinishInventory($input: SimFinishInventoryInputInput!) {\n  simFinishInventory(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "stage": None,
                "connectivityPlanId": None
            }
        }
    },
    "simFinishReady": {
        "query": "mutation simFinishReady($input: SimFinishReadyInputInput!) {\n  simFinishReady(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "stage": None,
                "connectivityPlanId": None
            }
        }
    },
    "simFinishTest": {
        "query": "mutation simFinishTest($input: SimFinishTestInputInput!) {\n  simFinishTest(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": None,
                "iccid": None,
                "stage": None,
                "connectivityPlanId": None
            }
        }
    },
    "simStartTest": {
        "query": "mutation simStartTest($input: SimInput!) {\n  simStartTest(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": "262199099999999999",
                "iccid": None
            }
        }
    },
    "simStartInventory": {
        "query": "mutation simStartInventory($input: SimInput!) {\n  simStartInventory(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": "262199099999999999",
                "iccid": None
            }
        }
    },
    "simStartLive": {
        "query": "mutation simStartLive($input: SimInput!) {\n  simStartLive(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": "262199099999999999",
                "iccid": None
            }
        }
    },
    "simStartSleep": {
        "query": "mutation simStartSleep($input: SimInput!) {\n  simStartSleep(input: $input) {\n    id\n    simId\n    requestedTime\n    changeType\n    state\n    completionTime\n    creationTime\n  }\n}",
        "variables": {
            "input": {
                "imsi": "262199099999999999",
                "iccid": None
            }
        }
    },
    "cancelSimOrder": {
        "query": "mutation cancelSimOrder($input: CancelSimOrderInputInput!) {\n  cancelSimOrder(input: $input) {\n    cancelSimOrder {\n    id\n    reason\n  }\n    created\n    updated\n  }\n}",
        "variables": {
            "input": {
                "id": "test_string",
                "reason": None
            }
        }
    },
    "submitSimOrder": {
        "query": "mutation submitSimOrder($input: SubmitSimOrderInputInput!) {\n  submitSimOrder(input: $input) {\n    id\n    created\n    updated\n  }\n}",
        "variables": {
            "input": {
                "id": "test_string"
            }
        }
    },
    "createSimOrder": {
        "query": "mutation createSimOrder($input: CreateSimOrderInputInput!) {\n  createSimOrder(input: $input) {\n    id\n    created\n    updated\n  }\n}",
        "variables": {
            "input": {
                "agreementId": None,
                "expectedSimProfiles": {
                    "packageQuantity": 0,
                    "packageSize": 0,
                    "unitSubscriptionId": "test_string"
                },
                "addresseeName": "test_string",
                "phoneNumber": "test_string",
                "expectedDeliveryAddress": {
                    "countryCode": "test_string",
                    "postalCode": "test_string",
                    "city": "test_string",
                    "street": "test_string",
                    "houseNumber": "test_string",
                    "apartmentNumber": None,
                    "state": None,
                    "addressLine2": None
                }
            }
        }
    },
    "editSimOrderProduct": {
        "query": "mutation editSimOrderProduct($input: EditSimOrderParamsInput!) {\n  editSimOrderProduct(input: $input) {\n    id\n    created\n    updated\n  }\n}",
        "variables": {
            "input": {
                "id": "test_string",
                "newExpected": {
                    "packageQuantity": 0,
                    "packageSize": 0,
                    "unitSubscriptionId": "test_string"
                }
            }
        }
    },
    "editSimOrderDeliverySettings": {
        "query": "mutation editSimOrderDeliverySettings($input: EditSimOrderDeliveryParamsInput!) {\n  editSimOrderDeliverySettings(input: $input) {\n    id\n    created\n    updated\n  }\n}",
        "variables": {
            "input": {
                "id": "test_string",
                "addresseeName": None,
                "phoneNumber": None,
                "companyName": None,
                "newDeliveryAddress": {
                    "countryCode": "test_string",
                    "postalCode": "test_string",
                    "city": "test_string",
                    "street": "test_string",
                    "houseNumber": "test_string",
                    "apartmentNumber": None,
                    "state": None,
                    "addressLine2": None
                }
            }
        }
    },
    "editSimOrderAlias": {
        "query": "mutation editSimOrderAlias($input: EditSimOrderAliasParamsInput!) {\n  editSimOrderAlias(input: $input) {\n    id\n    created\n    updated\n  }\n}",
        "variables": {
            "input": {
                "id": "test_string",
                "alias": "test_string"
            }
        }
    },
    "editSimOrderBusinessUnit": {
        "query": "mutation editSimOrderBusinessUnit($input: EditSimOrderBusinessUnitParamsInput!) {\n  editSimOrderBusinessUnit(input: $input) {\n    id\n    created\n    updated\n  }\n}",
        "variables": {
            "input": {
                "id": "test_string",
                "businessUnitId": "test_string"
            }
        }
    }
}
