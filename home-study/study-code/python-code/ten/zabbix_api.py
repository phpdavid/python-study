# coding=utf-8

import requests
import json


class ZabbixAPI(object):
    def __init__(self):
        self.url = 'http://192.168.92.130/api_jsonrpc.php'
        self.headers = {'Content-Type': 'application/json-rpc'}

    def login(self):
        params = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": "Admin",
                "password": "zabbix"
            },
            "id": 1,
            "auth": None
        }
        r = requests.post(self.url, data=json.dumps(params), headers=self.headers)
        print(r.json())

    def get_hosts(self):
        token = '845bbee4eed412e21bdfc5ba4261d368'
        params = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": [
                    "hostid",
                    "host"
                ],
                "selectInterfaces": [
                    "interfaceid",
                    "ip"
                ]
            },
            "id": 2,
            "auth": token
        }
        r = requests.get(self.url, data=json.dumps(params), headers=self.headers)
        print(r.text)


test = ZabbixAPI()
test.get_hosts()
