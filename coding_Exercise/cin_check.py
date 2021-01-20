#!/usr/bin/python3

import paramiko
from paramiko_expect import SSHClientInteraction
import serial
import os
import time
import argparse
import sys

def main():

	parser = argparse.ArgumentParser(description="description: Used to verify if CIN ports are up. No checks if in correct location.")

	#parser.add_argument(dest='c', help='TB ports that need to be checked on CIN. Format of \'tb3\' or \'tb4\'.')
	parser.add_argument('-c', dest='chassisSelection', help='Used to pick which chassis to check.')
	parser.add_argument('-l', dest='cards', help='List LC to check. Seperate list with a comma, no spaces.')
	parser.add_argument('-s', dest='show', help="Show console output.", action='store_true', default=False)
	parser.add_argument('-a', dest='skipConfig', help="Skip chassis config and just do checks. Default option is to apply config.", action='store_true', default=False)

	args = parser.parse_args() 
	chassisSelection = args.chassisSelection #what testbed's ports to check on cin.
	show = args.show
	cards = args.cards
	chassis = str(chassisSelection[-1])
	skip = args.skipConfig

	if len(chassisSelection) > 1:
		sys.exit("Too many char for tb name. Exiting...")
	
	if chassis != '3' and chassis != '4':
		sys.exit("Chassis selection invalid. Exiting...")

	if cards is None:
		#cards to test should be all?
		cards = '1,2,3,6,7,8,9'
	
	if chassis == '3':
		serialPort = '/dev/USB3'

	if chassis == '4':
		serialPort = '/dev/USB5'

	console = console_in(serialPort)
	cinIP = copy_network_config(chassis, console, skip)
	sys.exit("\r\r\tCIN config done. Please ping addresses to check connectivity. Exiting script.\r")

	ssh, client = ssh_connect(cinIP) #this needs to be from the cin

	if len(cards) == 1:
		cards = list(cards)
	if len(cards) != 1:
		cards = cards.split(',')

	cards.insert(0, '0') #add to the 0 position card '0'
	print()
	print('Checking below cards:\r')
	print('\t' + str(cards))

	lssueCards = check_cards(ssh, client, chassis, cards) #ssh to CIN, and cards to test

	if len(issueCards) != 0:
		the_issues(issueCards)
		
	else:
		print('\r\r\tAfter looking at requested cards, chassis is ready to test.')

	sys.exit("Exiting")

	return


def copy_network_config(chassis, console, skip):
	
	primaryIP = '10.23' + chassis + '.' +chassis + '0.5' #format of '10.23x.x0.5 /24 -> 10.233.30.5 for tb3
	
	if not skip:
		
		vlan = chassis+"0"
		hostApply = "hostname chassis" + chassis
		atpAdd = primaryIP[:-1]+'1'
		cfgFile = '23'+chassis+'_ip'
		priAddCMD = "ip addr " + str(primaryIP) + " 255.255.255.0"

		cfgFile = '23'+ chassis + '_ip'

		configAddresses = ['clear logging', '\r\n\r\n',"conf t", 'int hun4/1/0', 
							'no shut', "int hun4/1/0."+vlan, "encapsulation dot1Q "+vlan, "vrf forwarding Mgmt-intf", 
							priAddCMD, "no shut", "exit", "ip route 0.0.0.0 0.0.0.0 hun4/1/0", "end", "\r\n"]

		print("\r\tGetting to the correct location.\r")

		right_spot(console)

		print("\r\tStarting basic configuration for network access.\r")

		print("\rSending Console Commands\r\r")
		consoleOutput = []
		for command in configAddresses:
			console.flushInput() #flush input buffer
			console.flushOutput()#flush output buffer
			time.sleep(1)
			console.write(bytes(command + '\r\n', "utf-8"))
			output = console.readlines()
			for item in output:
				decodedOut = item.decode('utf-8')
				consoleOutput.append(decodedOut)
				print(decodedOut)
		
		print("\r\tBasic network application completed. Attempting to ping chassis from TFTP server.")
		time.sleep(5)
		response = os.system("ping -c 3 " + primaryIP) #ping chassis 3 times
		if response == 0: #Checks for the number of failures?
			print("\r\tCBR is able to ping test server. SSHing to chassis...")
			
		
		if response != 0:
			sys.exit("\r\tUnable to ping chassis. Verify connectivity and try again.")

		copyCfgCMD = 'copy tftp://'+atpAdd+'/cbr_cfg_files/'+cfgFile + ' running-config\r\r\r'	
		console.write(bytes(copyCfgCMD, 'utf-8'))
		output=''
		output=console.readlines()
		
		for returned in output:
			print(returned.decode('utf-8'))

	cinIP = primaryIP[:-1]+'3' #CIN IP for this tb's vlan
	return cinIP

def right_spot(console):
	
	i=0
	while i < 3:
		print("\r\nAttempt number " + str(i) + "\r\r")
		console.write(b'\r\n')
		output = console.readlines()

		for line in output:
			line = line.decode('utf-8')
		i+=1
		for item in output:
			item = item.decode('utf-8')
			print(item)
			if "#" in item: #if in priv exec mode
				if "(confi" in item: #exit config mode, check in priv exec, leave to global
					console.write(b'end\r\n')
					leaveConfig = console.readlines()
					for item in leaveConfig:
						item=item.decode('utf-8')
						if "#" in item:
							console.write(b"exit\r\n")
							print(console.readlines()) #TODO: output what's being sent to console. Comment out of final
							console.write(b"\r\n\r\n")
							print(console.readlines())
							time.sleep(1)
							console.write(b"en\r\n")
							print(console.readlines())
							break
				else: #if only in priv exec mode, break 3 times to skip checks
					i = 3
					break
				
			if ">" in item:
				console.write(b"en\r\n")
				enableCheck = console.readlines()
				for item in enableCheck:
					item = item.decode('utf-8') #!todo - untested
					if "password" in item.lower():
						console.write(b"cisco\r\n")
				print(console.readlines())

				break
			
			if "ress RETURN to" in item:
				console.write(b"\r\n\r\n")
				print(console.readlines())
				time.sleep(1)
				console.write(b"en\r\n")
				print(console.readlines())
				break

	console.write(b'\r\n') #used to get it to just kick out a line
	output = console.readlines()
	found = False
	for item in output:
		item = item.decode('utf-8')
		if "#"in item:
			found = True
			break
	if found == False:
		print("Failed to get to correct prompt. Re-run ONCE to see if corrected. Exiting Script")
		sys.exit("\r\tFailed to get to correct prompt. Re-run ONCE to see if corrected.")

def console_in(serialPort): #returns console connection information

	baud = 9600
	console = serial.Serial(serialPort, baud, timeout=1)
	print()
	print("\r\r\tChassis connected to console at" + serialPort) #print("here")
	print()
	
	return console

def ssh_connect(primaryIP):
	user = 'admin'
	passwd = 'WWTwwt1!'
	#prompt = 'WWT-ATP-CIN#'
	prompt = ".*# "
	primaryIP = '10.233.30.3'
	
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())#
	print( "\r\tAttempting to SSH into chassis at " + primaryIP + "...\r\r")
	
	i=0 
	for i in range(10):

		try:
			client.connect(hostname='10.233.30.3', username=user, password=passwd, allow_agent=False ,look_for_keys=False)
			print( "\n\tConnection established to " + str(primaryIP))
			break

		except:
			i+=1
			if i==9:	
				print( "SSH FAILED. Verify connection to Supervisor port NME0. Exiting Script")
				sys.exit('\n\tSSH failed. Exiting')
			time.sleep(10)
			print( "\n\tSSH attempt " + str(i) + " failed. waiting 10sec.\r")
	

	ssh = SSHClientInteraction(client, timeout=10, display=True) #!todo- change true
	ssh.send('\r\n')
	time.sleep(1)
	ssh.expect(prompt)
	ssh.current_output_clean
	return ssh, client

def send_command(ssh, client,  text):

	prompt = '.*CIN.*'

	ssh.send(text+'\r')
	#time.sleep(6)
	ssh.expect(prompt)
	
	
	output = ssh.current_output_clean
	output = output.splitlines()

	return output

def check_cards(ssh, client, chassis, cards):

	issueCards ={}
	issues = []
	shelfGroups = ['1','2','6','7'] #groupings for each rpd/vlan group TODO: THis is wrong
	ipGroup = ['8','9']

	for lc in cards:
		print('Looking at card ' + lc)
		for shelfIP in shelfGroups: #the 1,2,6,7
			passed = 2
			
			for port in ipGroup: #the .x8 and .x9

				address = '10.23'+chassis + '.' + lc+ '.'+ str(shelfIP) + str(port) #10.23C.S.LP
				pingCmd = 'ping '+ address
				output = send_command(ssh, client, pingCmd)
				
				for item in output:
					print(item)
					#input('hold')
					if " 100.00% packet loss" in item:
						print()
						print("\r\r\tIp " + address + " not reachable...\r\r")
						passed -= 1
						break

				if passed < 1:
					issueCards.update({lc:shelfIP})
		
		
		print()
		print(str(len(issueCards))+ " found on card " + lc + "...")
		input()


	return lssueCards

def the_issues(issueCards):

	pass

main()