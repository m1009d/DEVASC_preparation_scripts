#!/usr/bin/env python3

"""
https://developer.cisco.com/docs/sdwan/#!authentication

STEP1:
vManage REST API access control is based on sessions. All users will be able to
get a session after successfully logging in. The following are typical steps for
a user to consume the API:
Log in with a user name and password to establish a session:
POST /j_security_check with content type x-www-form-urlencoded.
The user name and password are submitted as j_username and j_password.
The session token is in the response http cookie, JSESSIONID={session hash}.

Code Snippet
  POST https://{vmanage-ip-address}/j_security_check
  Content-Type: application/x-www-form-urlencoded
  HTTP Body: "j_username={admin}&j_password={credential}"

STEP2:
Get a cross-site request forgery prevention token, which is required for
most POST operations:
GET /dataservice/client/token with content type application/json.
The JESSIONID={session hash} cookie is required to authenticate.
The XSRF token is in the response body. Use the XSRF token along with the
JESSIONID cookie for ongoing API requests.

Code Snippet
  GET https://{vmanage-ip-address}/dataservice/client/token
  Content-Type: application/json
  HTTP Header: "Cookie: JESSIONID={session hash id}"

STEP3:
Make an API request.
For non-whitelisted endpoints, the user needs to provide an API token
as a cookie: JESSIONID={session hash}.
For POST requests, the user also needs to provide the matching XSRF token.

Code Snippet
  https://{vmanage-ip-address}/dataservice/{api-endpoint-url}
  Content-Type: application/json
  HTTP Header: "Cookie: JESSIONID={session hashid}" "X-XSRF-TOKEN: {XSRF token}"


API requests header for GET/POST/PUT/DELETE are
    For vManage pre-19.2  - Session Cookie (jsessionid)
    For vManage post-19.2 - Session Cookie (jsessionid) and Token

It is mandatory to share the same session if multiple API requests are invoked
sequentially. The default session lifespan is 24 hours, and the session
inactivity timeout is 30 minutes.

The maximum concurrent session number is 250. The new session will invalidate
the least recently used session if the maximum concurrent session number is
reached.

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

import requests

# As we are working on a non-secured environment we can disable
# security warnings related to self-signed SSL certificate.
# Don't disable this in your production environment but rather
# configure your systems properly and secure.
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
disable_warnings(InsecureRequestWarning)


def get_auth_headers() -> dict:
    """
    Function will authenticate to the Cisco SD-WAN sandbox via the
    REST API and returns a dictionary containing the X-XSRF-TOKEN token and
    the session JESSIONID. Both parameters need to be set in the headers for
    all other subsequent requests to vManage 19.2+ version.
    """

    # STEP1 - get the session JESSIONID cookie
    # API URL - The session token is retrieved from the path '/j_security_check'
    API_URL = "https://sandbox-sdwan-1.cisco.com/j_security_check"

    # Storing passwords inside your scripts is not recommended but for the demo
    # purposes it is the easiest way.
    # One recommended way is to export your credentials as an environment variables
    # and then use these variables in your script.
    #
    # Example:
    # import os
    # PASSWORD = os.getenv('MY_SECURE_PASSWORD')
    #
    # Here the environment variable is called 'MY_SECURE_PASSWORD' which
    # contains your secret password.
    username = 'devnetuser'   # vManage username
    password = 'RG!_Yw919_83' # vManage password

    # Prepare the payload for the HTTP POST message
    # which includes the j_username and j_password
    payload = {
        'j_username' : username,
        'j_password' : password
    }

    # Create the requests session object
    session = requests.session()

    # Create the HTTP POST request
    # NOTE: verify=False is Not recommended TO USE in a production environment
    response = session.post(
        url=API_URL,
        data=payload,
        verify=False
    )

    # Raise an exception if the response is not OK
    if not response.ok:
        print(response.text)
        response.raise_for_status()

    # If the response contains <html> body, it meas there was an error
    if '<html>' in response.text:
        print(response.text)
        raise requests.HTTPError(
            'An error occured while getting the session cookie'
        )

    # JESSIONID cookie is in the response headers
    jsessionid = response.headers["Set-Cookie"].split(';')[0]

    # STEP2 - Get the XSFR token
    API_URL = "https://sandbox-sdwan-1.cisco.com/dataservice/client/token"
    xsfr_token_response = session.get(
        url=API_URL,
        verify=False
    )

    # Raise an exception if the response is not OK
    if not xsfr_token_response.ok:
        print(xsfr_token_response.text)
        xsfr_token_response.raise_for_status()

    # If the response contains <html> body, it meas there was an error
    if '<html>' in xsfr_token_response.text:
        print(xsfr_token_response.text)
        raise requests.HTTPError(
            'An error occured while getting the XSFR token'
        )

    # XSFR token is in the response body
    token = response.text

    # Return the authentication headers
    auth_headers = {
        'Cookie': jsessionid,
        'X-XSRF-TOKEN': token
    }

    return auth_headers
