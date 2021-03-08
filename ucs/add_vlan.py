#!/usr/bin/env python3

"""
This script will create a new VLAN 123
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

"""

# Import the Cisco UCS Python SDK library
from ucsmsdk.ucshandle import UcsHandle

# Import the FabricVlan module
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan


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

    # Query the class FabricLanCloud which contains VLANs info
    fabric_lan_cloud = handle.query_classid("FabricLanCloud")

    # Create the VLAN 123
    # 'id' and 'name' are mandatory arguments
    vlan123 = FabricVlan(
        parent_mo_or_dn=fabric_lan_cloud[0],
        name="vlan123",
        id="123"
    )

    # Add the VLAN 123 object to the object handle using the add_mo method.
    handle.add_mo(vlan123)

    # Commit the change to add the VLAN 123 to the UCS Manager
    handle.commit()

    # Logout from the server
    handle.logout()
