import serial
import time

"""This script is to automate and streamline initial setup/config for nexus devices out of box"""

"""Connecting to a specific 'COM' channel"""

def open_con(port, baudrate):
    console = serial.Serial(port=port, baudrate=baudrate, parity='N', stopbits=1, bytesize=8, timeout=8)
    if console.isOpen():
        return console
    else:
        return False

"""This execute's entered commands and translates it into bytes to get passed along to the device """

def run_cmd(console, cmd='\r\n', sleep=2):
    print('Sending command: ' + cmd)
    console.write(cmd.encode() + b'\n')
    time.sleep(sleep)

"""Reads and converts bytes from the console into human readable strings"""

def read_from_con(console):
    bytes_to_b_read = console.inWaiting()
    if bytes_to_b_read:
        output = console.read(bytes_to_b_read).decode()
        return output
    else:
        return False

"""Checks if 'POAP' process is present and skips it to proceed to the login prompt"""

def chk_poap_and_initconfig_dialog(console, sleep1=4):
    run_cmd(console, '\r\n')
    run_cmd(console, '\r\n', 3)
    poap_prompt = read_from_con(console)
    time.sleep(sleep1)
    if 'Would you like to enter the initial configuration dialog? [yes/no]:' in poap_prompt:
        run_cmd(console, 'no\r\n', 4)
        run_cmd(console, '\r\n')
        return True

    else:
        print("Bypassing initial config dialog...\nEntering 'User Exec mode'.........\nSwitch>")
        return


"""Setting standard Password during POAP phase(experimental)"""
# def chk_poap_pass(console):
#     run_cmd(console, '\r\n', 10)
#     run_cmd(console, '\r\n')
#     run_cmd(console, '\r\n')
#     poap_prompt1 = read_from_con(console)
#     if 'Enter the password for "admin":' in poap_prompt1:
#         run_cmd(console, '**Password\r\n', 5)
#         run_cmd(console, '**Password\r\n', 5)
#         run_cmd(console, 'no\r\n', 10)
#     else:
#         return False

"""Allows you to move from login prompt to enter privileged EXEC mode """

def access_switch(console, sleep=3):
    print("Entering 'Privileged Exec mode'....\nSwitch#")
    run_cmd(console, '\r\n')
    poap_prompt2 = read_from_con(console)
    time.sleep(sleep)
    if 'Switch>' in poap_prompt2:
        run_cmd(console, 'enable\r\n', 3)
        run_cmd(console, '\r\n', 3)
        return True
    else:
        return True


