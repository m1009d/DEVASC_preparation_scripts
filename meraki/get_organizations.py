#!/usr/bin/env python3

"""
This script will retrieve a list of all organizations via the Meraki
Dashboard API.

Meraki is setup hierarchically in a tree structure with Organizations at the
root of the tree. Organizations can have 1-N number of Networks.
Networks then organize Devices and provide for features based on the devices
assigned to that network.

API call to retrieve list of organizations:
/api/v0/organizations

For the authentication we need to use the authentication token
which can be obtained via the meraki dashboard.
Once the token is generated, it has to be encoded inside the
"X-Cisco-Meraki-API-Key" header field.

Example of returned data:
[
   {
      "id": <ORGANIZATION ID>,
      "name": <ORGANIZATION NAME>,
      "url": <URL TO ORGANIZATION OVERVIEW>"
   }
]

MERAKI DASHBOARD API Learning lab can be accessed here:
https://developer.cisco.com/learning/lab/meraki-02-dashboard-api/

Meraki Dashboard API documentation:
https://developer.cisco.com/meraki/api/
"""

import json
import requests


if __name__ == "__main__":

    # MERAKI API URL
    # only JSON encoding can be used
    API_URL = "https://api.meraki.com/api/v0/organizations"

    # Get the token via your Meraki dashboard webpage
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
    token = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

    # Prepare the headers for the HTTP GET message
    # with the token included.
    headers = {
        'Content-Type': 'application/json',
        'X-Cisco-Meraki-API-Key': token,
    }

    # Make the HTTP GET request to get all organizations
    response = requests.get(
        url=API_URL,
        headers=headers
    )

    # Raise an exception if the response is not OK
    if not response.ok:
        print(response.text)
        response.raise_for_status()

    # Convert the response message into a JSON datastructure
    orgs = response.json()

    # Print all organizations
    print(json.dumps(orgs, indent=4))
