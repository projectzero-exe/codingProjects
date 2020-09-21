import serial
import time

def open_con(port='com5', baudrate = 9600):
   console = serial.Serial(port='com5', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=8)
   if console.isOpen():
       return console
   else:
       return False

def run_cmd(console, cmd=str('\n'), sleep=2):
    print('Sending command: ' + cmd)
    console.write(cmd.encode() + b'\n')
    time.sleep(sleep)

def read_from_con(console):
    bytes_to_b_read =console.inWaiting()
    if bytes_to_b_read:
        output = console.read(bytes_to_b_read)
        return output.decode()
    else:
        return False

def chk_poap_and_initconfig_dialog(console):
    run_cmd(console, '\n', 6)
    poap_prompt = read_from_con(console)
    if 'Abort Power On Auto Provisioning' in poap_prompt:
        run_cmd(console, 'skip\r\n', 30)

    else:
        return False

# def chk_poap_pass(console):
#     run_cmd(console, '\r\n', 10)
#     run_cmd(console, '\r\n')
#     run_cmd(console, '\r\n')
#     poap_prompt1 = read_from_con(console)
#     if 'Enter the password for "admin":' in poap_prompt1:
#         run_cmd(console, 'Chase1234\r\n', 5)
#         run_cmd(console, 'Chase1234\r\n', 5)
#         run_cmd(console, 'no\r\n', 10)
#     else:
#         return False

def access_switch(console):
    run_cmd(console, '\r\n')
    run_cmd(console, '\r\n')
    poap_prompt2 = read_from_con(console)
    if 'switch login:' in poap_prompt2:
        run_cmd(console, 'admin\r\n',3)
        run_cmd(console, '\r\n', 3)


    else:
        return False