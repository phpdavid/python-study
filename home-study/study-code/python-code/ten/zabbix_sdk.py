# coding = utf-8

from pyzabbix import ZabbixAPI

zapi = ZabbixAPI('http://192.168.92.130')
zapi.login('Admin', 'zabbix')
for h in zapi.host.get(output='extend'):
    print(h['hostid'])
