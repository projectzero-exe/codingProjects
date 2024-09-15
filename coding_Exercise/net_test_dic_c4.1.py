from netmiko import ConnectHandler
import os
import csv

"""Opens a csv file with two columns [0]=interface [1]=Ip addresses;Removes the header row;
Creates a dictionary key value pair with {k}:port# and {v}:ip addresses"""

csv1 = input('Enter desired CSV file: ')
with open(csv1, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    ping_table = dict()
    for row in reader:
        ping_table[row[0]] = row[1]

"""device info to get passed along to netmiko Connecthandler"""

cisco_nxos = {
    'device_type': 'cisco_nxos',
    'host': '10.233.30.3',
    'username': 'admin',
    'password': 'WWTwwt1!',
    'port': 22,
    'secret': ''
    }


"""opens up remote connection to the target host and performs a ping test."""
connection = ConnectHandler(**cisco_nxos)
print('Performing Ping Test to CBr8 RPHY ports.....')
connection.enable()

"""Uses the key value pairs to ping ip addresses; 
flow control allows us to identify which ip's were not reachable and 
prints out which address and port were not reachable"""

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
