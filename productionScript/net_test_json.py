#! /usr/bin/env python3


from netmiko import ConnectHandler
import os
import json

cisco_nxos = {
    'device_type': 'cisco_nxos',
    'host': '10.233.30.3',
    'username': 'admin',
    'password': 'WWTwwt1!',
    'port': 22,
    'secret': ''
    }
choose_file = input("Enter desired JSON file: ")
    #print(data)
connection = ConnectHandler(**cisco_nxos)
print('Performing Ping Test to cBR8 RPHY ports.....')
connection.enable()

with open(choose_file, 'r') as jsonfile:
    data = json.load(jsonfile)


for k, v in data.items():
    output = connection.send_command('ping ' + v)
    if '0 packets received' in output:
        print('?' * 40)
        print(f">>>{k}<<<< Ping Unsuccessful. Address: {v}. Perform Layer 1 check..")
        print('?' * 40)
    else:
        print(f"{k} ^^^^PASSED^^^^ Ping Successful! Moving on to the next address..")

    #print(output)

print('Closing')
connection.disconnect()


