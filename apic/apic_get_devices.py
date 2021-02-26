#!/usr/bin/env python3

"""
This script will retrieve all the devices that are part of the
Cisco Sandbox APIC fabric.

The APIC REST API resource points to all the fabric devices:
/api/node/class/topology/pod-1/topSystem.json

For the authentication we need to use the authentication token
which can be obtained via the "apic_auth.py" script.
Once the token is available, it has to be encoded inside the
"Cookie" header field with value set to "APIC-Cookie=<token>".

Example of returned data:
{
    "totalCount": "1",
    "imdata": [
        {
            "topSystem": {
                "attributes": {
                    "address": "10.0.56.64",
                    "bootstrapState": "done",
                    "childAction": "",
                    "configIssues": "",
                    "controlPlaneMTU": "9000",
                    "currentTime": "2021-02-26T14:44:32.595+00:00",
                    "dn": "topology/pod-1/node-101/sys",
                    "enforceSubnetCheck": "yes",
                    "etepAddr": "0.0.0.0",
                    "fabricDomain": "ACI Fabric1",
                    "fabricId": "1",
                    "fabricMAC": "00:22:BD:F8:19:FF",
                    "id": "101",
                    "inbMgmtAddr": "0.0.0.0",
                    "inbMgmtAddr6": "::",
                    "inbMgmtAddr6Mask": "0",
                    "inbMgmtAddrMask": "0",
                    "inbMgmtGateway": "0.0.0.0",
                    "inbMgmtGateway6": "::",
                    "lcOwn": "local",
                    "modTs": "2021-02-24T15:27:38.831+00:00",
                    "mode": "unspecified",
                    "monPolDn": "uni/fabric/monfab-default",
                    "name": "leaf-1",
                    "nameAlias": "",
                    "nodeType": "unspecified",
                    "oobMgmtAddr": "0.0.0.0",
                    "oobMgmtAddr6": "::",
                    "oobMgmtAddr6Mask": "0",
                    "oobMgmtAddrMask": "0",
                    "oobMgmtGateway": "0.0.0.0",
                    "oobMgmtGateway6": "::",
                    "podId": "1",
                    "remoteNetworkId": "0",
                    "remoteNode": "no",
                    "rldirectMode": "no",
                    "role": "leaf",
                    "serial": "TEP-1-101",
                    "serverType": "unspecified",
                    "siteId": "0",
                    "state": "in-service",
                    "status": "",
                    "systemUpTime": "03:22:12:59.000",
                    "tepPool": "10.0.0.0/16",
                    "unicastXrEpLearnDisable": "yes",
                    "virtualMode": "no"
                }
            }
        }
    ]
}

APIC Sanbox can be found here:
https://sandboxapicdc.cisco.com/

ACI Programmability documentation:
https://developer.cisco.com/docs/aci/
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

# import the local function get_aci_token() from the apic_auth.py script
from apic_auth import get_aci_token


if __name__ == "__main__":

    # APIC API URI - with JSON encoding
    # XML encoding can be used as well
    APIC_URL = "https://sandboxapicdc.cisco.com/api/node/class/topology/pod-1/topSystem.json"

    # Get the token by calling the get_aci_token() function
    token = get_aci_token()

    # Prepare the headers for the HTTP GET message
    # with the token included inside the "Cookie".
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'APIC-cookie=' + token,
    }

    # Make the HTTP GET request to get all tenants
    response = requests.get(
        url=APIC_URL,
        headers=headers,
        verify=False
    )

    # Raise an exception if the response is not OK
    if not response.ok:
        print(json.dumps(response.json(), indent=4))
        response.raise_for_status()

    # Convert the response message into a JSON datastructure
    response_json = response.json()

    # Print the message
    print(json.dumps(response_json, indent=4))
