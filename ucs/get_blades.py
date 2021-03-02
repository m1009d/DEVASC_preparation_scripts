#!/usr/bin/env python3

"""
This script will retrieve a list of UCS Blades
via the Python SDK ucsmsdk library.

Python SDK for Cisco UCS installation can be done via pip:
    pip install ucsmsdk
or in a Python virtual environment:
    python3 -m venv ucsm
    cd ucsm
    source bin/activate
    pip install pip --upgrade
    pip install ucsmsdk

Python SDK for Cisco UCS GitHub page can be found here:
https://github.com/CiscoUcs/ucsmsdk

And more information can be found in the ucsmsdk_ug.rst file:
https://github.com/CiscoUcs/ucsmsdk/blob/master/docs/ucsmsdk_ug.rst

Cisco UCS API documentation is typically referred to as the UCS Object Model
documentation. The Object Model documentation is available with the UCS
Platform Emulator or online at
https://developer.cisco.com/site/ucs-mim-ref-api-picker/


Example output:
sys/chassis-3/blade-7
sys/chassis-3/blade-1
sys/chassis-3/blade-5
sys/chassis-3/blade-3
sys/chassis-4/blade-1
sys/chassis-4/blade-2
sys/chassis-4/blade-3
sys/chassis-4/blade-4
sys/chassis-4/blade-5
sys/chassis-4/blade-6
sys/chassis-4/blade-7
sys/chassis-4/blade-8
sys/chassis-5/blade-1
sys/chassis-5/blade-2
sys/chassis-5/blade-3
sys/chassis-5/blade-4
sys/chassis-5/blade-5
sys/chassis-5/blade-6
sys/chassis-5/blade-7
sys/chassis-5/blade-8
sys/chassis-6/blade-1
sys/chassis-6/blade-2
sys/chassis-6/blade-3
sys/chassis-6/blade-4
sys/chassis-6/blade-5
sys/chassis-6/blade-6
sys/chassis-6/blade-7
sys/chassis-6/blade-8
"""

# Import the Cisco UCS Python SDK library
from ucsmsdk.ucshandle import UcsHandle


if __name__ == "__main__":

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
    username = 'ucspe'   # UCS Manager username
    password = 'ucspe'   # UCS Manager password

    # Create a connection handle
    # You can reserve the Cisco DEVNET UCS sanbox and use it
    # for the following example.
    handle = UcsHandle("10.10.20.113", username, password)

    # Login to the server
    handle.login()

    # query the class computeBlade which contains blades info
    # and print the DN(Distinguished Name)
    blades = handle.query_classid("computeBlade")

    for blade in blades:
        print(blade.dn)

    # Logout from the server
    handle.logout()
