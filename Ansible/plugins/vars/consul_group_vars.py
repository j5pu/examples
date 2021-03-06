from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    vars: consul vars by Citius
'''

from ansible.module_utils._text import to_native
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.vars import BaseVarsPlugin
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.utils.vars import combine_vars
import requests
import base64
import yaml
CACHE = {}
PROJECT = {}


class VarsModule(BaseVarsPlugin):
    CONSUL_KV_URL = 'http://consul.service.consul:8500/v1/kv/'

    def kv_get(self, url, pref):
        # print(pref)
        result = {}
        if url in CACHE:
            return CACHE[url]
        try:
            r = requests.get(url)
            # print(r)
            if r.status_code == 404:
                return result
            parsed = r.json()
            if not isinstance(parsed, list):
                raise ValueError('Incorrect json: ' + r.content)

            def build_tree(branch, v, parts):
                # print(parts)
                if len(key_parts)==0:
                    return
                key = parts.pop(0)
                if key not in result:
                    if len(parts) == 0:
                        branch[key] = v
                    else:
                        if key not in branch:
                            branch[key] = dict()
                        build_tree(branch[key], v, parts)
                else:
                    build_tree(branch[key], v, parts)
            for item in parsed:
                fullkey = item['Key']
                # if 'istics-aggregation' in fullkey:
                #     print('!!!', fullkey)
                if '/' not in fullkey:
                    no_prefix_key = fullkey
                else:
                    no_prefix_key = fullkey[len(pref):]
                # print(fullkey)
                key_parts = [p for p in no_prefix_key.split('/') if p]
                value = base64.b64decode(item['Value']).decode("utf-8") if item['Value'] else None
                # print('result: ', result, 'value: ', value, 'key_parts: ', key_parts)
                build_tree(result, value, key_parts)
        except BaseException as e:
            raise AnsibleError('Error getting vars: %s' % to_native(e))
        CACHE[url] = result
        return result

    def get_vars(self, loader, path, entities):
        data = {}
        common_data = {}
        common_group_data = {}
        project_common_data = {}
        group_data = {}
        project = ''

        # print(path)

        for entity in entities:
            if entity.name == 'all':
                # print('group name is', entity.name )
                # print('entity dict is', entity.__dict__ )
                # print('group vars is', entity.vars )
                _path = 'inventory-json/common'
                url = self.CONSUL_KV_URL + _path+'?recurse'
                common_data = self.kv_get(url, _path)
                # print('common data:', common_data)
                data = combine_vars(common_data, entity.vars)
                if entity.vars['project']:
                    if project in PROJECT:
                        project = PROJECT[project]
                    else:
                        PROJECT[project] = entity.vars['project']

            elif isinstance(entity, Group):
                # print('group name is', entity.name )
                # print('entity dict is', entity.__dict__)
                # print('group vars is', entity.vars)
                _path = 'inventory-json/' + entity.name
                url = self.CONSUL_KV_URL + _path+'?recurse'
                common_group_data = self.kv_get(url, _path)
                # print('common group data:', common_group_data)

                _path = 'inventory-json/' + PROJECT[project] + '/common'
                url = self.CONSUL_KV_URL + _path+'?recurse'
                project_common_data = self.kv_get(url, _path)
                # print('common project data:', project_common_data)

                _path = 'inventory-json/' + PROJECT[project] + '/' + entity.name
                url = self.CONSUL_KV_URL + _path+'?recurse'
                group_data = self.kv_get(url, _path)
                # print('project group data:', group_data)

                data = common_group_data
                data = combine_vars(data, project_common_data)
                data = combine_vars(data, group_data)

            elif isinstance(entity, Host):
                # print('host', entity.name)
                pass
            else:
                raise AnsibleParserError("Supplied entity must be Host or Group, got %s instead" % (type(entity)))

        # print(data)
        return data