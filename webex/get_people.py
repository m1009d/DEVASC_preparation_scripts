#!/usr/bin/env python3

"""
This script will retrieve a list of people in your organization
via the Python requests library(REST API).

Cisco Webex Teams is an online collaboration solution to connect
people and teams through chat, voice, and video. With the Webex Teams app,
you gain access to secure virtual work spaces.
You also use messaging and file sharing with third-party app integrations.

The following REST API GET endpoints are used:

    # Get My Own Details
    https://webexapis.com/v1/people/me


You can try out the API directly in the Webex API Documentation:
https://developer.webex.com/docs/api/v1/people


Example output of my account info:
{
    "id": "<My account ID>",
    "emails": [
        "<my email address>"
    ],
    "phoneNumbers": [],
    "displayName": "Michal Test",
    "nickName": "Michal",
    "firstName": "Michal",
    "lastName": "Test",
    "orgId": "<The ID of the organization which owns this account>",
    "created": "2021-03-02T07:16:11.669Z",
    "lastModified": "2021-03-02T07:53:17.066Z",
    "timeZone": "Europe/Prague",
    "lastActivity": "2021-03-02T07:53:34.373Z",
    "status": "inactive",
    "type": "person"
}

"""

import json
import requests

# Get the Developer Access Token.
# Token is stored inside the "dev_access_token" variable
import webex_auth


def get_resource(**kwargs) -> dict:
    """
    HTTP GET request to the specified resource and return the dictionary data.
    Exit if there is an error.

    Pagination handling:
    If pagination is detected, the new key 'next_url' is added to the
    response_json dictionary.
    """

    response = requests.get(**kwargs)
    print(f"HTTP {response.request.method}: {response.url}")
    print(f'HTTP Status code: {response.status_code}')

    # Raise an exception if the response is not OK
    if not response.ok:
        print(response.text)
        response.raise_for_status()

    # Convert the reply to JSON
    response_json = response.json()

    # Check if the pagination is used and if yes, set the 'next_url' key
    # in the reponse dictionary
    next_link = response.headers.get('Link')
    if next_link:
        response_json['next_url'] = next_link.split(';')[0].strip('<>')

    # Return json parsed data as a python dictionary
    return response_json


if __name__ == "__main__":

    # Authentication HTTP header is used to identify the requesting user.
    # This header must include an access token.
    # This access token may be a Developer Access Token (limited duration),
    # Bot token, or an OAuth token from an Integration or Guest Issuer app.
    headers = {
        'Content-Type':  'application/json',
        'Accept':        'application/json',
        'Authorization': f'Bearer {webex_auth.dev_access_token}'
    }

    # In order to get information about my account, you can use the
    # 'https://webexapis.com/v1/people/me' URI:
    my_info = get_resource(
        url='https://webexapis.com/v1/people/me',
        headers=headers
    )

    # print the information about myself:
    print('Here is info about myself:')
    print(json.dumps(my_info, indent=4))

    # In order to get information about a specific person, you can use the
    # https://webexapis.com/v1/people URI with a specified ID params:
    params = {
        'id': my_info['id']
    }
    person_info = get_resource(
        url='https://webexapis.com/v1/people',
        headers=headers,
        params=params
    )

    print(f'Here is info about {my_info["displayName"]}:')
    print(json.dumps(my_info, indent=4))
