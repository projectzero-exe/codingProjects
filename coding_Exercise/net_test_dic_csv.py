# from netmiko import Netmiko
#
# connection = Netmiko(host='10.233.30.3', port='22', username='admin', password='WWTwwt1!', device_type='cisco_nxos')
from netmiko import ConnectHandler
import os
import csv

with open('ip.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    ping_table = dict()
    for row in reader:
        ping_table[row[0]] = row[1]
cisco_nxos = {
    'device_type': 'cisco_nxos',
    'host': '10.233.30.3',
    'username': 'admin',
    'password': 'WWTwwt1!',
    'port': 22,
    'secret': ''
    }

connection = ConnectHandler(**cisco_nxos)
print('Performing Ping Test to CBr8 RPHY ports.....')
connection.enable()

ping = ping_table
for k, v in ping.items():
    output = connection.send_command('ping ' + v)
    # need to investigate further to format output to show which ip did not work
    if '0 packets received' in output:
        print(f"{k} did not ping successful to address {v} check port")
    else:
        print(f"{k} pinged successful!")

    #print(output)
    
print('Closing')
connection.disconnect()
