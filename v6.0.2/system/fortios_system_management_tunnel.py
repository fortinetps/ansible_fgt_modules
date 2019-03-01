#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
# Copyright 2019 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_system_management_tunnel
short_description: Management tunnel configuration in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS by allowing the
      user to set and modify system feature and management_tunnel category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.2
version_added: "2.8"
author:
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Requires fortiosapi library developed by Fortinet
    - Run as a local_action in your playbook
requirements:
    - fortiosapi>=0.9.8
options:
    host:
       description:
            - FortiOS or FortiGate ip address.
       required: true
    username:
        description:
            - FortiOS or FortiGate username.
        required: true
    password:
        description:
            - FortiOS or FortiGate password.
        default: ""
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        default: root
    https:
        description:
            - Indicates if the requests towards FortiGate must use HTTPS
              protocol
        type: bool
        default: true
    system_management_tunnel:
        description:
            - Management tunnel configuration.
        default: null
        suboptions:
            allow-collect-statistics:
                description:
                    - Enable/disable collection of run time statistics.
                choices:
                    - enable
                    - disable
            allow-config-restore:
                description:
                    - Enable/disable allow config restore.
                choices:
                    - enable
                    - disable
            allow-push-configuration:
                description:
                    - Enable/disable push configuration.
                choices:
                    - enable
                    - disable
            allow-push-firmware:
                description:
                    - Enable/disable push firmware.
                choices:
                    - enable
                    - disable
            authorized-manager-only:
                description:
                    - Enable/disable restriction of authorized manager only.
                choices:
                    - enable
                    - disable
            serial-number:
                description:
                    - Serial number.
            status:
                description:
                    - Enable/disable FGFM tunnel.
                choices:
                    - enable
                    - disable
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Management tunnel configuration.
    fortios_system_management_tunnel:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      https: "False"
      system_management_tunnel:
        allow-collect-statistics: "enable"
        allow-config-restore: "enable"
        allow-push-configuration: "enable"
        allow-push-firmware: "enable"
        authorized-manager-only: "enable"
        serial-number: "<your_own_value>"
        status: "enable"
'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"

'''

from ansible.module_utils.basic import AnsibleModule


def login(data, fos):
    host = data['host']
    username = data['username']
    password = data['password']

    fos.debug('on')
    if 'https' in data and not data['https']:
        fos.https('off')
    else:
        fos.https('on')

    fos.login(host, username, password)


def filter_system_management_tunnel_data(json):
    option_list = ['allow-collect-statistics', 'allow-config-restore', 'allow-push-configuration',
                   'allow-push-firmware', 'authorized-manager-only', 'serial-number',
                   'status']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def system_management_tunnel(data, fos):
    vdom = data['vdom']
    system_management_tunnel_data = data['system_management_tunnel']
    filtered_data = filter_system_management_tunnel_data(system_management_tunnel_data)

    return fos.set('system',
                   'management-tunnel',
                   data=filtered_data,
                   vdom=vdom)


def fortios_system(data, fos):
    login(data, fos)

    if data['system_management_tunnel']:
        resp = system_management_tunnel(data, fos)

    fos.logout()
    return not resp['status'] == "success", resp['status'] == "success", resp


def main():
    fields = {
        "host": {"required": True, "type": "str"},
        "username": {"required": True, "type": "str"},
        "password": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "https": {"required": False, "type": "bool", "default": True},
        "system_management_tunnel": {
            "required": False, "type": "dict",
            "options": {
                "allow-collect-statistics": {"required": False, "type": "str",
                                             "choices": ["enable", "disable"]},
                "allow-config-restore": {"required": False, "type": "str",
                                         "choices": ["enable", "disable"]},
                "allow-push-configuration": {"required": False, "type": "str",
                                             "choices": ["enable", "disable"]},
                "allow-push-firmware": {"required": False, "type": "str",
                                        "choices": ["enable", "disable"]},
                "authorized-manager-only": {"required": False, "type": "str",
                                            "choices": ["enable", "disable"]},
                "serial-number": {"required": False, "type": "str"},
                "status": {"required": False, "type": "str",
                           "choices": ["enable", "disable"]}

            }
        }
    }

    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)
    try:
        from fortiosapi import FortiOSAPI
    except ImportError:
        module.fail_json(msg="fortiosapi module is required")

    fos = FortiOSAPI()

    is_error, has_changed, result = fortios_system(module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
