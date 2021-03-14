#!/usr/bin/env python3

"""
This script will create a new Webex Teams room (space)
via the Python requests library(REST API).

Cisco Webex Teams is an online collaboration solution to connect
people and teams through chat, voice, and video. With the Webex Teams app,
you gain access to secure virtual work spaces.
You also use messaging and file sharing with third-party app integrations.

The following REST API POST endpoints are used:

    # List all Rooms
    https://webexapis.com/v1/rooms

Note
The host name https://api.ciscospark.com has now been changed to
https://webexapis.com. The old https://api.ciscospark.com will continue to work.


You can try out the API directly in the Webex API Documentation:
https://developer.webex.com/docs/api/v1/rooms


Example after the room is created:
{
    "id": "<room ID>",
    "title": "DevNet Training",
    "type": "group",
    "isLocked": false,
    "lastActivity": "2021-03-02T09:57:14.483Z",
    "creatorId": "<creator ID>",
    "created": "2021-03-02T09:57:14.483Z",
    "ownerId": "<organization ID which owns the room>"
}
"""

import json
import requests

# Get the Developer Access Token.
# Token is stored inside the "dev_access_token" variable
import webex_auth


def post_resource(**kwargs) -> dict:
    """
    HTTP POST request to the specified resource and return the dictionary data.
    Exit if there is an error.
    """

    response = requests.post(**kwargs)
    print(f"HTTP {response.request.method}: {response.url}")
    print(f'HTTP Status code: {response.status_code}')

    # Raise an exception if the response is not OK
    if not response.ok:
        print(response.text)
        response.raise_for_status()

    # Convert the reply to JSON
    response_json = response.json()

    # Return json parsed data as a python dictionary
    return response_json


if __name__ == "__main__":

    # Authentication HTTP header is used to identify the requesting user.
    # This header must include an access token.
    # This access token may be a Developer Access Token (limited duration),
    # Bot token, or an OAuth token from an Integration or Guest Issuer app.
    headers = {
        'Accept':        'application/json',
        'Authorization': f'Bearer {webex_auth.dev_access_token}'
    }

    # Create a new room named "DevNet Training"
    params = {
        'title': 'DevNet Training'
    }

    resp = post_resource(
        url='https://webexapis.com/v1/rooms',
        headers=headers,
        json=params
    )
    print('Here is the response:')
    print(json.dumps(resp, indent=4))
