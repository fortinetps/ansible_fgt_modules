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
module: fortios_switch_controller_stp_settings
short_description: Configure FortiSwitch spanning tree protocol (STP) in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS by allowing the
      user to set and modify switch_controller feature and stp_settings category.
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
    switch_controller_stp_settings:
        description:
            - Configure FortiSwitch spanning tree protocol (STP).
        default: null
        suboptions:
            forward-time:
                description:
                    - Period of time a port is in listening and learning state (4 - 30 sec, default = 15).
            hello-time:
                description:
                    - Period of time between successive STP frame Bridge Protocol Data Units (BPDUs) sent on a port (1 - 10 sec, default = 2).
            max-age:
                description:
                    - Maximum time before a bridge port saves its configuration BPDU information (6 - 40 sec, default = 20).
            max-hops:
                description:
                    - Maximum number of hops between the root bridge and the furthest bridge (1- 40, default = 20).
            name:
                description:
                    - Name of global STP settings configuration.
            pending-timer:
                description:
                    - Pending time (1 - 15 sec, default = 4).
            revision:
                description:
                    - STP revision number (0 - 65535).
            status:
                description:
                    - Enable/disable STP.
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
  - name: Configure FortiSwitch spanning tree protocol (STP).
    fortios_switch_controller_stp_settings:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      https: "False"
      switch_controller_stp_settings:
        forward-time: "3"
        hello-time: "4"
        max-age: "5"
        max-hops: "6"
        name: "default_name_7"
        pending-timer: "8"
        revision: "9"
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


def filter_switch_controller_stp_settings_data(json):
    option_list = ['forward-time', 'hello-time', 'max-age',
                   'max-hops', 'name', 'pending-timer',
                   'revision', 'status']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def switch_controller_stp_settings(data, fos):
    vdom = data['vdom']
    switch_controller_stp_settings_data = data['switch_controller_stp_settings']
    filtered_data = filter_switch_controller_stp_settings_data(switch_controller_stp_settings_data)

    return fos.set('switch-controller',
                   'stp-settings',
                   data=filtered_data,
                   vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_switch_controller(data, fos):
    login(data, fos)

    if data['switch_controller_stp_settings']:
        resp = switch_controller_stp_settings(data, fos)

    fos.logout()
    return not is_successful_status(resp), \
        resp['status'] == "success", \
        resp


def main():
    fields = {
        "host": {"required": True, "type": "str"},
        "username": {"required": True, "type": "str"},
        "password": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "https": {"required": False, "type": "bool", "default": True},
        "switch_controller_stp_settings": {
            "required": False, "type": "dict",
            "options": {
                "forward-time": {"required": False, "type": "int"},
                "hello-time": {"required": False, "type": "int"},
                "max-age": {"required": False, "type": "int"},
                "max-hops": {"required": False, "type": "int"},
                "name": {"required": False, "type": "str"},
                "pending-timer": {"required": False, "type": "int"},
                "revision": {"required": False, "type": "int"},
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

    is_error, has_changed, result = fortios_switch_controller(module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
