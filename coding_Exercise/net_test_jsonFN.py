from netmiko import ConnectHandler
import os
import json

"""device info to get passed along to netmiko Connecthandler"""

cisco_nxos = {
    'device_type': 'cisco_nxos',
    'host': '192.233.30.3',
    'username': 'admin',
    'password': 'WWTwwt1!',
    'port': 22,
    'secret': ''
    }

"""Enter/Open's a json file ; Creates a dictionary key value pair with {k}:port# and {v}:ip addresses"""

choose_file = input('>>> ')
with open("choose_file", "r") as jsonfile:
    data = json.load(jsonfile)
#    print(data)

"""opens up remote connection to the target host and performs a ping test."""

connection = ConnectHandler(**cisco_nxos)
print('Performing Ping Test to CBr8 RPHY ports.....')
connection.enable()

"""Uses the key value pairs to ping ip addresses; 
flow control allows us to identify which ip's were not reachable; and 
prints out these address's and port's"""

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


