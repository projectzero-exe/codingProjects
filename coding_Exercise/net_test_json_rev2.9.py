#! /usr/bin/env python3


from netmiko import ConnectHandler
import json

cisco_nxos = {
    'device_type': 'cisco_nxos',
    'host': '10.233.30.3',
    'username': 'admin',
    'password': 'WWTwwt1!',
    'port': 22,
    'secret': ''
    }
tb = input("Enter desired Testbed '3' or '4': ")

choose_file = ""

if tb == '3':
    choose_file = "ip_json9_c3.json"

if tb == '4':
    choose_file = "ip_json9_c4.json"


connection = ConnectHandler(**cisco_nxos)
print('Performing Ping Test to cBR8 RPHY ports.....')
connection.enable()

with open(choose_file, 'r') as jsonfile:
    data = json.load(jsonfile)

failed_addr = {}

for k, v in data.items():
    output = connection.send_command('ping ' + v)
    if '0 packets received' in output:
        failed_addr.update({k: v})
        print('?' * 60)
        print(f">>>{k}<<<< Ping Unsuccessful. Address: {v}. Perform Layer 1 check..")
        print('?' * 60)
    else:
        print(f"{k} ^^^^PASSED^^^^ Ping Successful! Moving on to the next address..")

    #print(output)

print('Closing')
connection.disconnect()
print()

redo_test = True

while redo_test == True:

    if failed_addr != {}:
        print("These are the 'Failed' ports filtered for your convenience:\n")
        LC_P = "LineCard/Port"
        IPs = "IP Address"

        print(f"{LC_P:<5}   {IPs:<10}")
        for key, value in failed_addr.items():
            print(f"{key:<5}     {value:<10}\n")

        x = input("Would you like to retest failed IP's?\n Type 'y' to continue or hit 'n' key to quit: ")
        print(x)
        if x == 'y':
            print('Performing re-test to cBR8 RPHY ports.....')
            connection = ConnectHandler(**cisco_nxos)
            connection.enable()
            failed_addr1 = {}
            for k1, v1 in failed_addr.items():
                output = connection.send_command('ping ' + v1)
                if '0 packets received' in output:
                    failed_addr1.update({k1: v1})
                    print('?' * 60)
                    print(f">>>{k1}<<<< Ping Unsuccessful. Address: {v1}. Perform Layer 1 check..")
                    print('?' * 60)

                else:
                    print(f"{k1} ^^^^PASSED^^^^ Ping Successful! Moving on to the next address..")
                    redo_test = False
            failed_addr = failed_addr1
        else:
            redo_test = False
    else:
        print("PERFECT!!!!!! All optics have passed the Layer 1 test.")
        redo_test = False

print('Closing')
connection.disconnect()