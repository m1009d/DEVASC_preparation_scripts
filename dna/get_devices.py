#!/usr/bin/env python3

"""
This script will retrieve a list of all devices from the Cisco DNA Center.

Cisco DNA Center has a REST API that an authenticated and authorized user can
leverage to do operations over an HTTPS connection.
When the user autenticates, it receives a token that it needs to send in the
following requests in order to be authorized to execute calls to the API.

API call to get the auth token:
dna/system/api/v1/auth/token

API call to retrieve list of devices:
/dna/intent/api/v1/network-device

For the authentication we need to use the authentication token
which can be obtained via the HTTP POST call with username and
password for the DNA Center.
Once the token is generated, it has to be encoded inside the
"X-Auth-Token" header field.

Example of returned data:
{
    "response": [
        {
            "hostname": "asr1001-x.abc.inc",
            "apEthernetMacAddress": null,
            "apManagerInterfaceIp": "",
            "associatedWlcIp": "",
            "bootDateTime": "2021-02-16 21:06:52",
            "macAddress": "00:c8:8b:80:bb:00",
            "roleSource": "AUTO",
            "collectionInterval": "Global Default",
            "upTime": "25 days, 8:33:24.62",
            "deviceSupportLevel": "Supported",
            "softwareType": "IOS-XE",
            "softwareVersion": "16.3.2",
            "collectionStatus": "Managed",
            "errorCode": null,
            "errorDescription": null,
            "family": "Routers",
            "interfaceCount": "0",
            "lastUpdated": "2021-03-14 05:39:52",
            "lineCardCount": "0",
            "lineCardId": "",
            "locationName": null,
            "managedAtleastOnce": true,
            "managementIpAddress": "10.10.22.253",
            "memorySize": "NA",
            "platformId": "ASR1001-X",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "series": "Cisco ASR 1000 Series Aggregation Services Routers",
            "snmpContact": "",
            "snmpLocation": "",
            "tagCount": "0",
            "tunnelUdpPort": null,
            "uptimeSeconds": 2202806,
            "waasDeviceMode": null,
            "lastUpdateTime": 1615700392454,
            "description": "Cisco IOS Software [Denali], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.3.2, RELEASE SOFTWARE (fc4) Technical Support: http://www.cisco.com/techsupport Copyright (c) 1986-2016 by Cisco Systems, Inc. Compiled Tue 08-Nov-16 18:21 by m",
            "inventoryStatusDetail": "<status><general code=\"SUCCESS\"/></status>",
            "managementState": "Managed",
            "serialNumber": "FXS1932Q1SE",
            "type": "Cisco ASR 1001-X Router",
            "location": null,
            "role": "BORDER ROUTER",
            "instanceTenantId": "602bebe514710a00c98fa402",
            "instanceUuid": "6aad2ec7-d1d0-4605-bf32-f62266c5f53e",
            "id": "6aad2ec7-d1d0-4605-bf32-f62266c5f53e"
        }
    ],
    "version": "1.0"
}

DNA Center Platform API documentation:
https://developer.cisco.com/docs/dna-center/
"""

import json
import requests

# As we are working on a non-secured environment we can disable
# security warnings related to self-signed SSL certificate.
# Don't disable this in your production environment but rather
# configure your systems properly and secure.
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
disable_warnings(InsecureRequestWarning)


if __name__ == "__main__":

    # Cisco DNA Center Sandbox
    BASE_URL = "https://sandboxdnac.cisco.com/dna"

    # URL used to get the auth token
    AUTH_URL = BASE_URL + '/system/api/v1/auth/token'

    # URL used to get a list of devices
    DEV_URL = BASE_URL + '/intent/api/v1/network-device'

    # Storing passwords inside your scripts is not recommended but for the demo
    # purposes it is the easiest way.
    # One recommended way is to export your credentials as an environment
    # variables and then use these variables in your script.
    #
    # Example:
    # import os
    # PASSWORD = os.getenv('MY_SECURE_PASSWORD')
    #
    # Here the environment variable is called 'MY_SECURE_PASSWORD' which
    # contains your secret password.
    username = "devnetuser"
    password = "Cisco123!"

    # First we need to get the token via the HTTP POST method
    # NOTE: verify=False is Not recommended TO USE in a production environment
    response = requests.post(
        url=AUTH_URL,
        auth=(username,password),
        verify=False
    )

    # HTTP 200 code is expected if everything is OK, otherwise raise an error.
    if response.status_code != 200:
        print(response.text)
        raise requests.HTTPError(
            f'Got HTTP {response.status_code} code instead of 200! '\
            'Please check the response above for more information.'
        )

    # Token is stored in the response body inside the 'Token' key.
    token = response.json()['Token']

    # Prepare the headers with the token included.
    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': token,
    }

    # Make the HTTP GET request in order to get a list of all devices
    # NOTE: verify=False is Not recommended TO USE in a production environment
    response = requests.get(
        url=DEV_URL,
        headers=headers,
        verify=False
    )

    # HTTP 200 code is expected if everything is OK, otherwise raise an error.
    if response.status_code != 200:
        print(response.text)
        raise requests.HTTPError(
            f'Got HTTP {response.status_code} code instead of 200! '\
            'Please check the response above for more information.'
        )

    # Store all devices in a dictionary
    all_devices = response.json()

    # Get list of hostnames and print the result
    print('Bellow is the list of hostnames found in DNA Center:')
    for device in all_devices['response']:
        print(device['hostname'])
