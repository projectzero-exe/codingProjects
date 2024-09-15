# from netmiko import Netmiko
#
# connection = Netmiko(host='10.233.30.3', port='22', username='admin', password='WWTwwt1!', device_type='cisco_nxos')
from netmiko import ConnectHandler
import os
import csv

with open('ip_lc9.csv', 'r') as f:
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
        print('?' * 40)
        print(f">>>{k}<<<< Ping Unsuccessful. Address: {v}. Perform Layer 1 check..")
        print('?' * 40)
    else:
        print(f"{k} ^^^^PASSED^^^^ Ping Successful! Moving on to the next address..")

    #print(output)
    
print('Closing')
connection.disconnect()
