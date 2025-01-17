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
module: fortios_user_device
short_description: Configure devices in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS by allowing the
      user to set and modify user feature and device category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.2
version_added: "2.9"
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
    state:
        description:
            - Indicates whether to create or remove the object
        choices:
            - present
            - absent
    user_device:
        description:
            - Configure devices.
        default: null
        suboptions:
            alias:
                description:
                    - Device alias.
                required: true
            avatar:
                description:
                    - Image file for avatar (maximum 4K base64 encoded).
            category:
                description:
                    - Device category.
                choices:
                    - none
                    - amazon-device
                    - android-device
                    - blackberry-device
                    - fortinet-device
                    - ios-device
                    - windows-device
            comment:
                description:
                    - Comment.
            mac:
                description:
                    - Device MAC address(es).
            master_device:
                description:
                    - Master device (optional). Source user.device.alias.
            tagging:
                description:
                    - Config object tagging.
                suboptions:
                    category:
                        description:
                            - Tag category. Source system.object-tagging.category.
                    name:
                        description:
                            - Tagging entry name.
                        required: true
                    tags:
                        description:
                            - Tags.
                        suboptions:
                            name:
                                description:
                                    - Tag name. Source system.object-tagging.tags.name.
                                required: true
            type:
                description:
                    - Device type.
                choices:
                    - unknown
                    - android-phone
                    - android-tablet
                    - blackberry-phone
                    - blackberry-playbook
                    - forticam
                    - fortifone
                    - fortinet-device
                    - gaming-console
                    - ip-phone
                    - ipad
                    - iphone
                    - linux-pc
                    - mac
                    - media-streaming
                    - printer
                    - router-nat-device
                    - windows-pc
                    - windows-phone
                    - windows-tablet
                    - other-network-device
            user:
                description:
                    - User name.
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Configure devices.
    fortios_user_device:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      https: "False"
      state: "present"
      user_device:
        alias: "<your_own_value>"
        avatar: "<your_own_value>"
        category: "none"
        comment: "Comment."
        mac: "<your_own_value>"
        master_device: "<your_own_value> (source user.device.alias)"
        tagging:
         -
            category: "<your_own_value> (source system.object-tagging.category)"
            name: "default_name_11"
            tags:
             -
                name: "default_name_13 (source system.object-tagging.tags.name)"
        type: "unknown"
        user: "<your_own_value>"
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
from ansible.module_utils.connection import Connection
from ansible.module_utils.network.fortios.fortios import FortiOSHandler
from ansible.module_utils.network.fortimanager.common import FAIL_SOCKET_MSG


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


def filter_user_device_data(json):
    option_list = ['alias', 'avatar', 'category',
                   'comment', 'mac', 'master_device',
                   'tagging', 'type', 'user']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def underscore_to_hyphen(data):
    if isinstance(data, list):
        for elem in data:
            elem = underscore_to_hyphen(elem)
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[k.replace('_', '-')] = underscore_to_hyphen(v)
        data = new_data

    return data


def user_device(data, fos):
    vdom = data['vdom']
    state = data['state']
    user_device_data = data['user_device']
    filtered_data = underscore_to_hyphen(filter_user_device_data(user_device_data))

    if state == "present":
        return fos.set('user',
                       'device',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('user',
                          'device',
                          mkey=filtered_data['alias'],
                          vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_user(data, fos):

    if data['user_device']:
        resp = user_device(data, fos)

    return not is_successful_status(resp), \
        resp['status'] == "success", \
        resp


def main():
    fields = {
        "host": {"required": False, "type": "str"},
        "username": {"required": False, "type": "str"},
        "password": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "https": {"required": False, "type": "bool", "default": True},
        "state": {"required": True, "type": "str",
                  "choices": ["present", "absent"]},
        "user_device": {
            "required": False, "type": "dict",
            "options": {
                "alias": {"required": True, "type": "str"},
                "avatar": {"required": False, "type": "str"},
                "category": {"required": False, "type": "str",
                             "choices": ["none", "amazon-device", "android-device",
                                         "blackberry-device", "fortinet-device", "ios-device",
                                         "windows-device"]},
                "comment": {"required": False, "type": "str"},
                "mac": {"required": False, "type": "str"},
                "master_device": {"required": False, "type": "str"},
                "tagging": {"required": False, "type": "list",
                            "options": {
                                "category": {"required": False, "type": "str"},
                                "name": {"required": True, "type": "str"},
                                "tags": {"required": False, "type": "list",
                                         "options": {
                                             "name": {"required": True, "type": "str"}
                                         }}
                            }},
                "type": {"required": False, "type": "str",
                         "choices": ["unknown", "android-phone", "android-tablet",
                                     "blackberry-phone", "blackberry-playbook", "forticam",
                                     "fortifone", "fortinet-device", "gaming-console",
                                     "ip-phone", "ipad", "iphone",
                                     "linux-pc", "mac", "media-streaming",
                                     "printer", "router-nat-device", "windows-pc",
                                     "windows-phone", "windows-tablet", "other-network-device"]},
                "user": {"required": False, "type": "str"}

            }
        }
    }

    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)

    legacy_mode = 'host' in module.params and module.params['host'] is not None and \
                  'username' in module.params and module.params['username'] is not None and \
                  'password' in module.params and module.params['password'] is not None

    if not legacy_mode:
        if module._socket_path:
            connection = Connection(module._socket_path)
            fos = FortiOSHandler(connection)

            is_error, has_changed, result = fortios_user(module.params, fos)
        else:
            module.fail_json(**FAIL_SOCKET_MSG)
    else:
        try:
            from fortiosapi import FortiOSAPI
        except ImportError:
            module.fail_json(msg="fortiosapi module is required")

        fos = FortiOSAPI()

        login(module.params, fos)
        is_error, has_changed, result = fortios_user(module.params, fos)
        fos.logout()

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
