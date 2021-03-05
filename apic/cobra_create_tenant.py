#!/usr/bin/env python3

"""
Steps to install the ACI Cobra SDK in a Python virtual environment
    python -m vevn acicobra_testing
    cd acicobra_testing
    source bin/activate
    python -m pip install --upgrade pip   # upgrade pip to the newest version
    pip install acicobra

The Cisco ACI uses an information-model-based architecture
(Management Information Tree [MIT]) in which the model describes all the
information that can be controlled by a management process.
Object instances are referred to as managed objects (MOs).
To learn more about the MIT and MOs, you can visit this page:
https://cobra.readthedocs.io/en/latest/understanding.html

Getting Started with the Cisco APIC Python API:
https://cobra.readthedocs.io/en/latest/getting-started.html
"""


from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
from cobra.mit.request import ConfigRequest
from cobra.model.fv import Tenant


if __name__ == "__main__":

    # APIC API URI
    APIC_URL = "https://sandboxapicdc.cisco.com"

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
    USERNAME = "admin"
    PASSWORD = "ciscopsdt"

    # Connecting and Authenticating - create a new session and login
    loginSession = LoginSession(APIC_URL, USERNAME, PASSWORD)
    mo_dir = MoDirectory(loginSession)
    mo_dir.login()

    # Build a new configuration object
    tenant_name = 'Tenant1'
    uni_mo = mo_dir.lookupByDn('uni')
    new_mo = Tenant(uni_mo, name=tenant_name)

    # Create a new config request
    tenant_cfg = ConfigRequest()
    tenant_cfg.addMo(new_mo)

    # Commit the config request
    mo_dir.commit(tenant_cfg)

    # Get the tenant by is's name
    tenant = mo_dir.lookupByDn(f'uni/{tenant_name}')
