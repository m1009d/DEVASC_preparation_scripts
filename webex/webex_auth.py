"""
This script contains only the Webex Teams Developer Access Token variable.
You can import this file in your scripts and use the variable directly there.
Advantage of this simple file is that you have just one file with your token
variable. If you need to use a new token variable, you just need to change
this file and other scripts will work without any further change.
Remember to store this file securely.

Note:
This developer token should be used only for experimentation and testing,
do not use it in any production applications.
This token has a short lifetime—only 12 hours after logging.

In order to get the Developer Access Token which will be used in our REST API
calls, first you need a Webex Teams account, which can be created for free here:
https://developer.webex.com/
Once the you have the account, click on the Documentation link, then select
Getting Started in REST API section and scroll down to the Accounts and
Authentication section, where you should see your Developer Access Token
(hidden with stars).
https://developer.webex.com/docs/api/getting-started
Copy this token and set it here in the "dev_access_token" variable.


Storing passwords inside your scripts is not recommended but for the demo
purposes it is the easiest way.
One recommended way is to export your credentials as an environment variables
and then use these variables in your script.

Example:
import os
PASSWORD = os.getenv('dev_access_token')

Here the environment variable is called 'dev_access_token' which
contains your secret password.
"""

# Set the Developer Access Token
dev_access_token="Y2I0YjcyMTItZDk4OC00MTZkLWFkZWItYjIxNzczM2Y3YjFhMDBhZDIzN2MtNzY5_P0A1_636b97a0-b0af-4297-b0e7-480dd517b3f9"
