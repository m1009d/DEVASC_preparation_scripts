#!/usr/bin/env python3

"""
This script will retrieve a list of Webex Teams rooms (spaces)
via the Python requests library(REST API).

Cisco Webex Teams is an online collaboration solution to connect
people and teams through chat, voice, and video. With the Webex Teams app,
you gain access to secure virtual work spaces.
You also use messaging and file sharing with third-party app integrations.

The following REST API GET endpoints are used:

    # List all Rooms
    https://api.ciscospark.com/v1/rooms

    # Get Room Details
    https://api.ciscospark.com/v1/rooms/{roomId}

    # Get Room Meeting Details
    https://api.ciscospark.com/v1/rooms/{roomId}/meetingInfo

Note: The host name https://api.ciscospark.com has now been changed to
https://webexapis.com. The old https://api.ciscospark.com will continue to work.

You can try out the API directly in the Webex API Documentation:
https://developer.webex.com/docs/api/v1/rooms


Example output of all rooms:
{
    "items": [
        {
            "id": "<A unique identifier for the room>",
            "title": "<room (space) name>",
            "type": "group",
            "isLocked": false,
            "lastActivity": "2021-03-02T07:54:15.799Z",
            "creatorId": "<The ID of the person who created this room>",
            "created": "2021-03-02T07:54:15.799Z",
            "ownerId": "<The ID of the organization which owns this room>"
        }
    ]
}

Example output of a specific room info:
{
    "id": "<A unique identifier for the room>",
    "title": "<room (space) name>",
    "type": "group",
    "isLocked": false,
    "lastActivity": "2021-03-02T07:54:15.799Z",
    "creatorId": "<The ID of the person who created this room>",
    "created": "2021-03-02T07:54:15.799Z",
    "ownerId": "<The ID of the organization which owns this room>"
}

Example output of a meeting room info:
{
    "roomId": "<A unique identifier for the room>",
    "meetingLink": "https://meet5.webex.com/m/<uique_identifier>",
    "sipAddress": "<meetingNumber>@meet5.webex.com",
    "meetingNumber": "<meetingNumber>"
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

    # In order to simulate the pagination, we can limit the max. number
    # of items returned by setting the param value:
    params = {
        "max": 1
    }

    # Get all rooms
    all_rooms = get_resource(
        url='https://api.ciscospark.com/v1/rooms',
        headers=headers,
        params=params
    )
    print('Here are all rooms:')
    print(json.dumps(all_rooms, indent=4))

    # store the first room id:
    room_id = all_rooms['items'][0]['id']
    room_name = all_rooms['items'][0]['title']

    # Pagination handling:
    # The Webex APIs implement the RFC5988 Web Linking standard for pagination.
    # This function will check the response headers for 'Link' field and if
    # it's found, function will fetch the data and append in the reply.
    next_url = all_rooms.get('next_url')
    while next_url:
        # Get all rooms from next link url
        all_rooms = get_resource(
            url=next_url,
            headers=headers
        )
        next_url = all_rooms.get('next_url')

        # Print all rooms from the next link url
        print(json.dumps(all_rooms, indent=4))

    # Get information about a specific room from:
    # https://api.ciscospark.com/v1/rooms/{roomId} URI:
    room_info = get_resource(
        url=f'https://api.ciscospark.com/v1/rooms/{room_id}',
        headers=headers
    )

    # print the information about requests room ID:
    print(f'Here is information about the {room_name}:')
    print(json.dumps(room_info, indent=4))

    # In order to get information about a specific room meeting details,
    # you can use the
    # https://api.ciscospark.com/v1/rooms/{roomId}/meetingInfo URI:
    meeting_info = get_resource(
        url=f'https://api.ciscospark.com/v1/rooms/{room_id}/meetingInfo',
        headers=headers
    )

    # print the information about requests room ID:
    print(f'Here is the meeting information from the {room_name}:')
    print(json.dumps(meeting_info, indent=4))
