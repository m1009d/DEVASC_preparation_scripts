#!/usr/bin/env python3

"""
This script will retrieve all the tenants that are part of the
Cisco Sandbox APIC fabric.

The APIC REST API resource points to all the fabric tenants:
/api/node/class/fvTenant.json

For the authentication we need to use the authentication token
which can be obtained via the "apic_auth.py" script.
Once the token is available, it has to be encoded inside the
"Cookie" header field with value set to "APIC-Cookie=<token>".

Example of returned data:
{
    "totalCount": "1",
    "imdata": [
        {
            "fvTenant": {
                "attributes": {
                    "annotation": "",
                    "childAction": "",
                    "descr": "",
                    "dn": "uni/tn-Shore-Test-1",
                    "extMngdBy": "",
                    "lcOwn": "local",
                    "modTs": "2021-02-22T20:32:11.546+00:00",
                    "monPolDn": "uni/tn-common/monepg-default",
                    "name": "Shore-Test-1",
                    "nameAlias": "",
                    "ownerKey": "",
                    "ownerTag": "",
                    "status": "",
                    "uid": "15374"
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
    APIC_URL = "https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json"

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
