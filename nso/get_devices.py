#!/usr/bin/env python3

"""
This script will retrieve a list of all devices managed by Cisco NSO
via the RESTCONF interface.

The RESTCONF API is a standardized REST interface as defined in RFC 8040
and provides a number of improvements over the proprietary and legacy
REST interface, including the support for auto-generating Swagger/OpenAPI
documents from YANG.
Both XML and JSON data formats are supported by the Cisco NSO RESTCONF interface.
NOTE: The REST API has been deprecated since NSO 5.1 and
is scheduled to be removed in NSO 5.3.

RESTCONF resources and endpoints are available under:
/restconf

For the authentication we need to use the simple authentication as
the Basic Auth base 64 encoded value which is provided by requests
Python module.

Example of returned data:
{
  "tailf-ncs:devices": {
    "global-settings": {
      "trace-dir": "/var/log/ncs"
    },
    "authgroups": {
      "group": [
        {
          "name": "labadmin",
          "default-map": {
            "remote-name": "cisco",
            "remote-password": "$9$5VBSdqF01tEhn2D8jp7YTmlDKnrlPdsQT3x0dBiiArc=",
            "remote-secondary-password": "$9$dbTOp+yHX7/sx0SZ/Rl9V+REmqK7BP/N2wLEdaUlMdA="
          }
        }
      ]
    },
    "device-group": [
      {
        "name": "ALL",
        "device-group": ["ASA-DEVICES", "IOS-DEVICES", "NXOS-DEVICES", "XR-DEVICES"],
        "member": ["core-rtr01", "core-rtr02", "dist-rtr01", "dist-rtr02", "dist-sw01", "dist-sw02", "edge-firewall01", "internet-rtr01"],
        "ned-id": [
          {
            "id": "cisco-asa-cli-6.12:cisco-asa-cli-6.12"
          },
          {
            "id": "cisco-nx-cli-5.20:cisco-nx-cli-5.20"
          },
          {
            "id": "cisco-iosxr-cli-7.32:cisco-iosxr-cli-7.32"
          },
          {
            "id": "cisco-ios-cli-6.67:cisco-ios-cli-6.67"
          }
        ],
        "tailf-ncs-alarms:alarm-summary": {
          "indeterminates": 0,
          "criticals": 0,
          "majors": 3,
          "minors": 0,
          "warnings": 0
        }
      },
      {
        "name": "ASA-DEVICES",
        "device-name": ["edge-firewall01"],
        "member": ["edge-firewall01"],
        "ned-id": [
          {
            "id": "cisco-asa-cli-6.12:cisco-asa-cli-6.12"
          }
        ],
        "tailf-ncs-alarms:alarm-summary": {
          "indeterminates": 0,
          "criticals": 0,
          "majors": 0,
          "minors": 0,
          "warnings": 0
        }
      },
      {
        "name": "IOS-DEVICES",
        "device-name": ["dist-rtr01", "dist-rtr02", "internet-rtr01"],
        "member": ["dist-rtr01", "dist-rtr02", "internet-rtr01"],
        "ned-id": [
          {
            "id": "cisco-ios-cli-6.67:cisco-ios-cli-6.67"
          }
        ],
        "tailf-ncs-alarms:alarm-summary": {
          "indeterminates": 0,
          "criticals": 0,
          "majors": 0,
          "minors": 0,
          "warnings": 0
        }
      },
      {
        "name": "NXOS-DEVICES",
        "device-name": ["dist-sw01", "dist-sw02"],
        "member": ["dist-sw01", "dist-sw02"],
        "ned-id": [
          {
            "id": "cisco-nx-cli-5.20:cisco-nx-cli-5.20"
          }
        ],
        "tailf-ncs-alarms:alarm-summary": {
          "indeterminates": 0,
          "criticals": 0,
          "majors": 0,
          "minors": 0,
          "warnings": 0
        }
      },
      {
        "name": "XR-DEVICES",
        "device-name": ["core-rtr01", "core-rtr02"],
        "member": ["core-rtr01", "core-rtr02"],
        "ned-id": [
          {
            "id": "cisco-iosxr-cli-7.32:cisco-iosxr-cli-7.32"
          }
        ],
        "tailf-ncs-alarms:alarm-summary": {
          "indeterminates": 0,
          "criticals": 0,
          "majors": 3,
          "minors": 0,
          "warnings": 0
        }
      }
    ],
    "mib-group": [
      {
        "name": "snmp",
        "mib-module": ["SNMP*"]
      }
    ],
    "device": [
      {
        "name": "core-rtr01",
        "address": "10.10.20.173",
        "ssh": {
          "host-key-verification": "none"
        },
        "authgroup": "labadmin",
        "device-type": {
          "cli": {
            "ned-id": "cisco-iosxr-cli-7.32:cisco-iosxr-cli-7.32",
            "protocol": "telnet"
          }
        },
        "commit-queue": {
          "queue-length": 0
        },
        "active-settings": {
          "connect-timeout": 20,
          "read-timeout": 20,
          "write-timeout": 20,
          "ssh-keep-alive": {
            "interval": 20,
            "count": 3
          },
          "ned-keep-alive": {
            "count": 3
          },
          "connect-retries": {
            "attempts": 0,
            "timeout": 3
          },
          "trace": "false",
          "trace-output": "file",
          "ned-settings": {
            "use-junos-rollback": false
          },
          "commit-queue": {
            "enabled-by-default": false
          },
          "session-pool": {
            "idle-time": 30
          },
          "no-overwrite": {
            "enabled-by-default": false
          },
          "out-of-sync-commit-behaviour": "reject"
        },
        "state": {
          "oper-state": "disabled",
          "oper-state-error-tag": "noconnection",
          "transaction-mode": "ned",
          "last-transaction-id": "1000000055+2000000002",
          "admin-state": "unlocked"
        },
        "capability": [
          {
            "uri": "http://tail-f.com/ned/cisco-ios-xr",
            "revision": "2020-12-04",
            "module": "tailf-ned-cisco-ios-xr"
          },
          {
            "uri": "http://tail-f.com/ned/cisco-ios-xr-stats",
            "revision": "2020-12-04",
            "module": "tailf-ned-cisco-ios-xr-stats"
          },
          {
            "uri": "http://tail-f.com/ns/ncs-ned/cli-allow-abbrev-keys"
          },
          {
            "uri": "http://tail-f.com/ns/ncs-ned/show-partial?path-format=cmd-path-modes-only"
          },
          {
            "uri": "http://tail-f.com/ns/ncs-ned/show-stats-path"
          },
          {
            "uri": "urn:ietf:params:netconf:capability:with-defaults:1.0?basic-mode=trim"
          },
          {
            "uri": "urn:ietf:params:xml:ns:yang:ietf-interfaces",
            "revision": "2014-05-08",
            "module": "ietf-interfaces"
          },
          {
            "uri": "urn:ietf:params:xml:ns:yang:ietf-ip",
            "revision": "2014-06-16",
            "module": "ietf-ip"
          }
        ],
        "module": [
          {
            "name": "ietf-interfaces",
            "revision": "2014-05-08"
          },
          {
            "name": "ietf-ip",
            "revision": "2014-06-16"
          },
          {
            "name": "tailf-ned-cisco-ios-xr",
            "revision": "2020-12-04"
          },
          {
            "name": "tailf-ned-cisco-ios-xr-stats",
            "revision": "2020-12-04"
          }
        ],
        "platform": {
          "name": "ios-xr",
          "version": "6.3.1",
          "model": "IOS XRv",
          "serial-number": "N/A"
        },
        "config": {
          "ietf-yang-library:yang-library": {
            "module-set": [
              {
                "name": "common",
                "module": [
                  {
                    "name": "ietf-interfaces",
                    "revision": "2014-05-08",
                    "namespace": "urn:ietf:params:xml:ns:yang:ietf-interfaces",
                    "feature": ["arbitrary-names", "if-mib", "pre-provisioning"]
                  },
                  {
                    "name": "ietf-ip",
                    "revision": "2014-06-16",
                    "namespace": "urn:ietf:params:xml:ns:yang:ietf-ip",
                    "feature": ["ipv4-non-contiguous-netmasks", "ipv6-privacy-autoconf"]
                  },
                  {
                    "name": "tailf-ned-cisco-ios-xr",
                    "revision": "2020-12-04",
                    "namespace": "http://tail-f.com/ned/cisco-ios-xr"
                  },
                  {
                    "name": "tailf-ned-cisco-ios-xr-stats",
                    "namespace": "http://tail-f.com/ned/cisco-ios-xr-stats"
                  }
                ],
                "import-only-module": [
                  {
                    "name": "tailf-ned-cisco-ios-xr-id",
                    "revision": "",
                    "namespace": "http://tail-f.com/ned/cisco-ios-xr-id"
                  }
                ]
              }
            ],
            "schema": [
              {
                "name": "common",
                "module-set": ["common"]
              }
            ],
            "datastore": [
              {
                "name": "ietf-datastores:running",
                "schema": "common"
              },
              {
                "name": "ietf-datastores:intended",
                "schema": "common"
              },
              {
                "name": "ietf-datastores:operational",
                "schema": "common"
              }
            ],
            "content-id": "e66e7cf457e6f0fc5f4b7b6f1848ce71"
          },
          "ietf-yang-library:modules-state": {
            "module-set-id": "e66e7cf457e6f0fc5f4b7b6f1848ce71",
            "module": [
              {
                "name": "ietf-interfaces",
                "revision": "2014-05-08",
                "namespace": "urn:ietf:params:xml:ns:yang:ietf-interfaces",
                "feature": ["arbitrary-names", "if-mib", "pre-provisioning"],
                "conformance-type": "implement"
              },
              {
                "name": "ietf-ip",
                "revision": "2014-06-16",
                "namespace": "urn:ietf:params:xml:ns:yang:ietf-ip",
                "feature": ["ipv4-non-contiguous-netmasks", "ipv6-privacy-autoconf"],
                "conformance-type": "implement"
              },
              {
                "name": "tailf-ned-cisco-ios-xr",
                "revision": "2020-12-04",
                "namespace": "http://tail-f.com/ned/cisco-ios-xr",
                "conformance-type": "implement"
              },
              {
                "name": "tailf-ned-cisco-ios-xr-id",
                "revision": "",
                "namespace": "http://tail-f.com/ned/cisco-ios-xr-id",
                "conformance-type": "import"
              },
              {
                "name": "tailf-ned-cisco-ios-xr-stats",
                "revision": "",
                "namespace": "http://tail-f.com/ned/cisco-ios-xr-stats",
                "conformance-type": "implement"
              }
            ]
          }
        }
    ...

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
    API_URL = "https://sandbox-nso-1.cisco.com/restconf/data/tailf-ncs:devices"

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

    # Print all devices
    print(response.text)
