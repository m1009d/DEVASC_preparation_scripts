#!/usr/bin/env python3

"""
A Cisco NSO service contains a description of any capability of the network,
from simply defining a new loopback interface on a device and its configuration,
to defining L3VPNs throughout the whole network.

This script will retrieve a list of all the services that are configured
via the RESTCONF interface.

The RESTCONF API is a standardized REST interface as defined in RFC 8040
and provides a number of improvements over the proprietary and legacy
REST interface, including the support for auto-generating Swagger/OpenAPI
documents from YANG.
Both XML and JSON data formats are supported by the Cisco NSO RESTCONF interface.
NOTE: The REST API has been deprecated since NSO 5.1 and
is scheduled to be removed in NSO 5.3.

RESTCONF resources and endpoints are available under:
/restconf/data/tailf-ncs:services/

For the authentication we need to use the simple authentication as
the Basic Auth base 64 encoded value which is provided by requests
Python module.

Example of returned data:
{
  "tailf-ncs:services": {
    "global-settings": {
      "collect-forward-diff": true
    },
    "logging": {
      "logger": [
        {
          "name": "default",
          "log-entry-level": "info"
        }
      ]
    },
    "loopbackdevnet:loopbackdevnet": [
      {
        "name": "tpl1",
        "modified": {
          "devices": ["ios0"]
        },
        "directly-modified": {
          "devices": ["ios0"]
        },
        "device-list": ["ios0"],
        "device": "ios0",
        "loopback-number": 0,
        "ip-address": "1.1.1.1"
      },
      {
        "name": "tpl2",
        "modified": {
          "devices": ["iosxr0"]
        },
        "directly-modified": {
          "devices": ["iosxr0"]
        },
        "device-list": ["iosxr0"],
        "device": "iosxr0",
        "loopback-number": 0,
        "ip-address": "2.2.2.2"
      }
    ]
  }
}


You can find the new DevNet NSO sandbox here
https://devnetsandbox.cisco.com/RM/Diagram/Index/aa07cf66-b756-4424-99c1-4a93aa42c913?diagramType=Topology
"""

import requests

# As we are working on a non-secured environment we can disable
# security warnings related to self-signed SSL certificate.
# Don't disable this in your production environment but rather
# configure your systems properly and secure.
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
disable_warnings(InsecureRequestWarning)


if __name__ == "__main__":

    # Sandbox users can directly access the NSO instance via public URL below:
    API_URL = "https://sandbox-nso-1.cisco.com"\
              "/restconf/data/tailf-ncs:services/"

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
    username = 'developer'
    password = 'Services4Ever'

    # Prepare the headers for the HTTP GET message
    # Both XML and JSON data formats are supported.
    # To use JSON data format we need to setup the headers with
    # the 'Content-Type': 'application/yang-data+json'
    headers = {
        'Content-Type': 'application/yang-data+json',
    }

    # Make the HTTP GET request to get all devices
    # requests generates a Basic Auth base 64 encoded value for us
    # by specifing the auth argument.
    response = requests.get(
        url=API_URL,
        auth=(username, password),
        headers=headers,
        verify=False
    )
    print(f"HTTP GET: {response.url}")
    print(f'HTTP Status code: {response.status_code}')

    # Raise an exception if the response is not OK
    if not response.ok:
        print(response.text)
        response.raise_for_status()

    # Print the result
    # From the output you can see the service name definition and to which
    # devices is each service applied.
    print(response.text)
