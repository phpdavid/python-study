# encoding = utt-8
import sys
import logging
from pyzabbix import ZabbixAPI

# 开启zabbix日志
stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.DEBUG)
log = logging.getLogger('pyzabbix')
log.addHandler(stream)
log.setLevel(logging.DEBUG)

zapi = ZabbixAPI('http://192.168.92.130')
zapi.login('Admin', 'zabbix')
