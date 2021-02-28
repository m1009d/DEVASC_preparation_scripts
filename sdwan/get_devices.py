#!/usr/bin/env python3

"""
This script will retrieve a list of all devices
via the SD-WAN REST API.

API call to retrieve list devices inside of an organization:
/dataservice/device

For the authentication the Session Cookie (jsessionid) and Token
needs to be set in the requests session headers.
Please see more details in the sdwan_auth.py file.

Example of returned data:
{
    "header": {
        "generatedOn": 1614489339685,
        "viewKeys": {
            "uniqueKey": [
                "system-ip"
            ],
            "preferenceKey": "grid-Device"
        },
        "columns": [
            {
                "title": "Hostname",
                "property": "host-name",
                "display": "iconAndText",
                "iconProperty": "device-type",
                "hideable": false,
                "icon": [
                    {
                        "key": "vmanage",
                        "value": "images/vmanage_table.png"
                    },
                    {
                        "key": "vedge",
                        "value": "images/vedge_table.png"
                    },
                    {
                        "key": "vedge-vbond",
                        "value": "images/vedge-vbond_table.png"
                    },
                    {
                        "key": "vsmart",
                        "value": "images/vsmart_table.png"
                    },
                    {
                        "key": "vbond",
                        "value": "images/vbond_table.png"
                    }
                ],
                "width": 150,
                "dataType": "string"
            },
            {
                "title": "State",
                "property": "state",
                "display": "iconAndToolTip",
                "iconProperty": "state",
                "toolTipProperty": "state_description",
                "defaultPropertyKey": "reachability",
                "defaultPropertyValue": "reachable",
                "icon": [
                    {
                        "key": "green",
                        "value": "images/device_state_green.png"
                    },
                    {
                        "key": "red",
                        "value": "images/device_state_red.png"
                    },
                    {
                        "key": "yellow",
                        "value": "images/device_state_yellow.png"
                    },
                    {
                        "key": "default",
                        "value": "images/device_state_other.png"
                    }
                ],
                "width": 20,
                "dataType": "string"
            },
            {
                "title": "System IP",
                "property": "system-ip",
                "hideable": false,
                "width": 110,
                "dataType": "ipv4"
            },
            {
                "title": "Reachability",
                "property": "reachability",
                "display": "multiColumns",
                "color": [
                    {
                        "key": "reachable",
                        "value": "616161",
                        "property": "reachability"
                    },
                    {
                        "key": "unreachable",
                        "value": "ef5350",
                        "property": "reachability"
                    },
                    {
                        "key": "auth-failed",
                        "value": "ffb300",
                        "property": "reachability"
                    },
                    {
                        "key": "staging",
                        "value": "ffb300",
                        "property": "validity"
                    }
                ],
                "width": 150,
                "minWidth": 150,
                "dataType": "string"
            },
            {
                "title": "Site ID",
                "property": "site-id",
                "width": 70,
                "dataType": "numberStr"
            },
            {
                "title": "Device Model",
                "property": "device-model",
                "display": "multiColumns",
                "hideable": false,
                "width": 100,
                "dataType": "deviceModel"
            },
            {
                "title": "BFD",
                "property": "bfdSessions",
                "width": 75,
                "minWidth": 65,
                "dataType": "numberStr"
            },
            {
                "title": "Control",
                "property": "controlConnections",
                "width": 75,
                "minWidth": 65,
                "dataType": "numberStr"
            },
            {
                "title": "Version",
                "property": "version",
                "width": 150,
                "dataType": "string"
            },
            {
                "title": "Up Since",
                "property": "uptime-date",
                "displayFormat": "DD MMM YYYY h:mm:ss A z",
                "inputFormat": "unix-time",
                "width": 200,
                "dataType": "date"
            },
            {
                "title": "Chassis Number/ID",
                "property": "uuid",
                "hideable": false,
                "width": 220,
                "dataType": "string"
            },
            {
                "title": "Device Groups",
                "property": "device-groups",
                "width": 100,
                "dataType": "array"
            },
            {
                "title": "Connected vManage",
                "property": "connectedVManages",
                "width": 500,
                "dataType": "array"
            }
        ],
        "fields": [
            {
                "property": "host-name",
                "dataType": "string",
                "display": "iconAndText"
            },
            {
                "property": "state",
                "dataType": "string",
                "display": "iconAndToolTip"
            },
            {
                "property": "system-ip",
                "dataType": "ipv4"
            },
            {
                "property": "reachability",
                "dataType": "string",
                "display": "multiColumns"
            },
            {
                "property": "site-id",
                "dataType": "numberStr"
            },
            {
                "property": "device-model",
                "dataType": "deviceModel",
                "display": "multiColumns"
            },
            {
                "property": "bfdSessions",
                "dataType": "numberStr"
            },
            {
                "property": "controlConnections",
                "dataType": "numberStr"
            },
            {
                "property": "version",
                "dataType": "string"
            },
            {
                "property": "number-vsmart-peers",
                "dataType": "number"
            },
            {
                "property": "uptime-date",
                "dataType": "date"
            },
            {
                "property": "uuid",
                "dataType": "string"
            },
            {
                "property": "board-serial",
                "dataType": "string"
            },
            {
                "property": "device-groups",
                "dataType": "array"
            },
            {
                "property": "connectedVManages",
                "dataType": "array"
            },
            {
                "property": "lastupdated",
                "dataType": "date"
            }
        ]
    },
    "data": [
        {
            "deviceId": "10.10.1.1",
            "system-ip": "10.10.1.1",
            "host-name": "vmanage",
            "reachability": "reachable",
            "status": "normal",
            "personality": "vmanage",
            "device-type": "vmanage",
            "timezone": "UTC",
            "device-groups": [
                "\"No groups\""
            ],
            "lastupdated": 1613879699736,
            "domain-id": "0",
            "board-serial": "969E8292C5E64183A2563B7A3605B67D",
            "certificate-validity": "Valid",
            "max-controllers": "0",
            "uuid": "81ac6722-a226-4411-9d5d-45c0ca7d567b",
            "controlConnections": "1",
            "device-model": "vmanage",
            "version": "19.2.2",
            "connectedVManages": [
                "\"10.10.1.1\""
            ],
            "site-id": "101",
            "latitude": "37.666684",
            "longitude": "-122.777023",
            "isDeviceGeoData": false,
            "platform": "x86_64",
            "uptime-date": 1613271960000,
            "statusOrder": 4,
            "device-os": "next",
            "validity": "valid",
            "state": "green",
            "state_description": "All daemons up",
            "model_sku": "None",
            "local-system-ip": "10.10.1.1",
            "total_cpu_count": "2",
            "testbed_mode": false,
            "layoutLevel": 1
        },
        {
            "deviceId": "10.10.1.5",
            "system-ip": "10.10.1.5",
            "host-name": "vsmart",
            "reachability": "reachable",
            "status": "normal",
            "personality": "vsmart",
            "device-type": "vsmart",
            "timezone": "UTC",
            "device-groups": [
                "\"No groups\""
            ],
            "lastupdated": 1613272187182,
            "domain-id": "1",
            "board-serial": "4E500CAE354B4341B322C5DA4BD7588A",
            "certificate-validity": "Valid",
            "uuid": "f7b49da3-383e-4cd5-abc1-c8e97d345a9f",
            "controlConnections": "9",
            "device-model": "vsmart",
            "version": "19.2.2",
            "connectedVManages": [
                "\"10.10.1.1\""
            ],
            "site-id": "101",
            "ompPeers": "4",
            "latitude": "37.666684",
            "longitude": "-122.777023",
            "isDeviceGeoData": false,
            "platform": "x86_64",
            "uptime-date": 1592300940000,
            "statusOrder": 4,
            "device-os": "next",
            "validity": "valid",
            "state": "green",
            "state_description": "All daemons up",
            "model_sku": "None",
            "local-system-ip": "10.10.1.5",
            "total_cpu_count": "0",
            "testbed_mode": false,
            "layoutLevel": 2
        },
        {
            "deviceId": "10.10.1.3",
            "system-ip": "10.10.1.3",
            "host-name": "vbond",
            "reachability": "reachable",
            "status": "normal",
            "personality": "vbond",
            "device-type": "vbond",
            "timezone": "UTC",
            "device-groups": [
                "\"No groups\""
            ],
            "lastupdated": 1613272182530,
            "board-serial": "7AC124B4AED648EB99B9900DD56A405C",
            "certificate-validity": "Valid",
            "uuid": "ed0863cb-83e7-496c-b118-068e2371b13c",
            "device-model": "vedge-cloud",
            "version": "19.2.2",
            "connectedVManages": [
                "\"10.10.1.1\""
            ],
            "site-id": "101",
            "latitude": "37.666684",
            "longitude": "-122.777023",
            "isDeviceGeoData": false,
            "platform": "x86_64",
            "uptime-date": 1601996340000,
            "statusOrder": 4,
            "device-os": "next",
            "validity": "valid",
            "state": "green",
            "state_description": "All daemons up",
            "model_sku": "None",
            "local-system-ip": "10.10.1.3",
            "total_cpu_count": "4",
            "linux_cpu_count": "1",
            "testbed_mode": false,
            "layoutLevel": 3
        }
    ]
}

The Cisco SD-WAN always on sandbox can be accessed here:
https://devnetsandbox.cisco.com/RM/Diagram/Index/\
fa7f7ef9-e224-4ee7-a3fe-0f25506e9db9?diagramType=Topology

Manage REST APIs Command Reference can be found here:
https://sdwan-docs.cisco.com/Product_Documentation/Command_Reference/\
Command_Reference/vManage_REST_APIs/vManage_REST_APIs_Overview/\
Using_the_vManage_REST_APIs

You can explore the API documentation and even try it out by logging
into the apidocs resource on your vManage platform as:
https://<vmanage_host>:<vmanage_port>/apidocs
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

# Local import from the sdwan_auth.py file
from sdwan_auth import get_auth_headers


if __name__ == "__main__":

    # Get the requests.session() object which contain the JESSIONID
    # session ID as well as the X-XSRF-TOKEN.
    auth_headers = get_auth_headers()

    # SD-WAN API URL
    # only JSON encoding can be used
    API_URL = "https://sandbox-sdwan-1.cisco.com/dataservice/device"

    # HTTP GET to get a list of all devices
    response = requests.get(
        url=API_URL,
        headers=auth_headers,
        verify=False
    )
    print(f"HTTP GET: {response.url}")

    # Raise an exception if the response is not OK
    if not response.ok:
        print(response.text)
        response.raise_for_status()

    # If the response contains <html> body, it meas there was an error
    if '<html>' in response.text:
        print(response.text)
        raise requests.HTTPError(f'An error occured while getting {API_URL}')

    # Everything is OK, print all devices
    print(json.dumps(response.json(), indent=4))
