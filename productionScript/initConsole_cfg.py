import json
#import textfsm
import serial
import time

"""This script is to automate and streamline initial setup/config for devices(e.g. NX-OS, IOS-XE) out of box"""

"""Connecting to a specific 'COM' channel"""

def open_con(port='', baudrate=9600):
    console = serial.Serial(port, baudrate, parity='N', stopbits=1, bytesize=8, timeout=8)
    if console.isOpen():
        return console
    else:
        return False

"""This execute's entered commands and translates it into bytes to get passed along to the device """

def run_cmd(console, cmd='\r\n', sleep=1):
    print('Sending command: ' + cmd)
    console.write(cmd.encode('utf-8') + b'\r\n')
    time.sleep(sleep)

"""Reads and converts bytes from the console into human readable strings"""

def read_from_con(console):
    bytes_to_b_read = console.inWaiting()
    if bytes_to_b_read:
        output = console.read(bytes_to_b_read).decode()
        return output
    else:
        return "Issues with reading from prompt"

"""Checks if 'POAP' process is present and skips it to proceed to the login prompt"""

def chk_poap_and_initconfig_dialog(console):
    run_cmd(console, '\r\n')
    run_cmd(console, '\r\n', 3)
    poap_prompt = read_from_con(console)
    time.sleep(1)
    if 'Would you like to enter the initial configuration dialog? [yes/no]:' in poap_prompt:
        run_cmd(console, 'no\r\n', 4)
        run_cmd(console, '\r\n')
        return True

    else:
        print("Bypassing initial config dialog...\nEntering 'User Exec mode'.........\nSwitch>")
        return


"""Setting standard Password during POAP phase(experimental)"""
def chk_poap_pass(console):
     run_cmd(console, '\r\n', 10)
     run_cmd(console, '\r\n')
     run_cmd(console, '\r\n')
     poap_prompt1 = read_from_con(console)
     if 'Enter the password for "admin":' in poap_prompt1:
         run_cmd(console, '**Password\r\n', 5)
         run_cmd(console, '**Password\r\n', 5)
         run_cmd(console, 'no\r\n', 10)
     else:
         return False

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


'''small function to retrieve serial number from the device and return the speficied serial'''
def getserialnumber(console, cmds='show inv', ele=0, sleep=2):
    run_cmd(console, cmds, sleep)
    output = read_from_con(console)
    js = output.split()[ele]
    return js


'''Checks results from the console and ensures that the response is either '#' or '>' '''
def parsercheck(console, cmdp='\r\n', sleep=1):
    while True:
        run_cmd(console, cmdp, sleep)
        output = read_from_con(console)
        print(output)
        output2 = output.split()
        if "Router>" in output2:
            run_cmd(console, "enable")
            break
        if "Router(config)#" in output2:
            run_cmd(console, "end")
            break
        if "Router#" in output2:
            break



'''Executes a defined list of commands in a for loop'''
def run_list_cmd(console, rlc="", sleep=2):
    run_cmd(console, "term len 0")
    for cmd_ls in rlc:
        run_cmd(console, cmd_ls, sleep)
        print(read_from_con(console))


"""This snippet parses retrun CLI output and converts it into a json data structure and converts 
it into a usable python object("txttp" is to specify which template to use; "readcli"  """
 def parsing_txtFSM(console, txttp='', cmdCLI=''):
     run_cmd(console, "term len 0", sleep=1)
     run_cmd(console, cmdCLI)
     readcli = read_from_con(console)
     with open(txttp) as t:
         results_template = textfsm.TextFSM(t)
         content= readcli
         presults = results_template.ParseTextToDicts(content)
         res = json.dumps(presults, indent=2)
         print(res)
         res1 = json.loads(res)
         #print(res1)
         return res1

 """"This function is designed for devices running IOS-XE. This function will retrieve cli output and convert serial number info into a JSON format"""

def getSerialnum(console, cmdSP1="show inventory | i PID"):
    lsfieldserial = []
    #column = ["PID", "VID", "SN"]
    run_cmd(console, cmd="term len 0")
    run_cmd(console, cmdSP1)
    readcliSP1 = read_from_con(console)
    # print(readcliSP1)
    description = list(readcliSP1.replace(" ", "").split("\r\n"))
    lsfieldserial.append(description)

    # print(lsfieldserial[0])
    # x = lsfieldserial
    x1 = lsfieldserial[0][3].split(",")
    # print(x)
    """have to keep working to improve the extraction process currently script only will retrieve serial number from a NCS4202 device"""
    # for i in range(len(lsfield1)):
    #     if i == 0:
    #         for x in range(len(fields1)):
    #             dicts0[fields1[x]] = lsfield1[i][x]
    #
    #     elif i == 1:
    #         for x in range(len(fields1)):
    #             dicts1[fields1[x]] = lsfield1[i][x]
    #
    #     elif i == 2:
    #         for x in range(len(fields1)):
    #             dicts2[fields1[x]] = lsfield1[i][x]
    #
    #     elif i == 3:
    #         for x in range(len(fields1)):
    #             dicts3[fields1[x]] = lsfield1[i][x]
    #     elif i == 4:
    #         for x in range(len(fields1)):
    #             dicts4[fields1[x]] = lsfield1[i][x]
    #     elif i == 5:
    #         for x in range(len(fields1)):
    #             dicts5[fields1[x]] = lsfield1[i][x]
    return x1[2].replace("SN:", "").replace("PID:", "").replace("VID:", "")

""""This function is designed for devices running IOS-XE. This function will retrieve cli output and convert "show plaform" info into a JSON format"""
def showplattoDict(console, cmdSP="show platform"):

    run_cmd(console, cmd="term len 0")
    run_cmd(console, cmdSP, sleep=2)
    readcliSP = read_from_con(console)
    print(readcliSP)
    #resultant dictionary
    dicts0 = {}
    dicts1 = {}
    dicts2 = {}
    dicts3 = {}
    dicts4 = {}
    dicts5 = {}
    dicts6 = {}
    dicts7 = {}
    # fields in the sample file
    fields1 = ['Slot', 'Type', 'State', 'Insert time']
    fields2 = ['Slot', 'CPLD Version', 'Firmware Ver']
    # intermediary list to process lsfield 1 and 2
    lsfield = []

    description = list(readcliSP.strip().split("\r\n"))
    lsfield.append(description)
    # print(lsfield[0])
    # print("#" * 225)
    #strips begin and ending of extra spaces and splits it into sub-elements of 4  per element
    x = [ele.strip().split(None, 4) for ele in lsfield[0] if ele != []]
    # print(x)

    # lsfield_p = [ele for ele in lsfield if ele != []]
    # print(lsfield)
    # print("#" * 200)
    # print(lsfield_p)
    # print("#" * 200)
    lsfield1 = x[7:13]
    # print("#" * 200)
    lsfield2 = x[16:18]
    # print("#" * 200)
    # print(lsfield1)
    # print("#" * 200)
    # print(lsfield2)
    # print("#" * 200)
    for i in range(len(lsfield1)):
        if i == 0:
            for x in range(len(fields1)):
                dicts0[fields1[x]] = lsfield1[i][x]

        elif i == 1:
            for x in range(len(fields1)):
                dicts1[fields1[x]] = lsfield1[i][x]

        elif i == 2:
            for x in range(len(fields1)):
                dicts2[fields1[x]] = lsfield1[i][x]

        elif i == 3:
            for x in range(len(fields1)):
                dicts3[fields1[x]] = lsfield1[i][x]
        elif i == 4:
            for x in range(len(fields1)):
                dicts4[fields1[x]] = lsfield1[i][x]
        elif i == 5:
            for x in range(len(fields1)):
                dicts5[fields1[x]] = lsfield1[i][x]
    # print(lsfield2)
    for i in range(len(lsfield2)):
        if i == 0:
            for x in range(len(fields2)):
                dicts6[fields2[x]] = lsfield2[i][x]

        elif i == 1:
            for x in range(len(fields2)):
                dicts7[fields2[x]] = lsfield2[i][x]

    r = []
    r.append(dicts0)
    r.append(dicts1)
    r.append(dicts2)
    r.append(dicts3)
    r.append(dicts4)
    r.append(dicts5)
    r.append(dicts6)
    r.append(dicts7)
    result = json.loads(json.dumps(r))
    print()
    print(r)

    return result

"""this is a new concept that needs more work. function will reload device wait a specified time and will handle initial sys configs"""
def reloadsequence(console, cmdre="reload", savecfg="", sleep=500):
    run_cmd(console, cmdre, sleep)
    run_cmd(console)
    read = read_from_con(console)
    print(read)
    ct = 0
    while ct < 6:
        if "System configuration has been modified. Save?" in read:
            run_cmd(console, savecfg)
            read1 = read_from_con(console)
            print(read1)
            if "Proceed with reload? [confirm]" in read1:
                run_cmd(console, "\n\n")
                ct +=1
            else:
                print("Check prompt !!!! FAILURE level 3 OCCURRED")
                ct += 1
        elif "% Please answer 'yes' or 'no'." in read:
            run_cmd(console, savecfg)
            read2 = read_from_con(console)
            if "Proceed with reload? [confirm]" in read2:
                run_cmd(console, "\n\n")
                ct += 1
            else:
                print("Check prompt !!!! FAILURE level 2 OCCURRED")
                ct += 1

        elif "Proceed with reload? [confirm]" in read:
            run_cmd(console, "\n\n")
            ct += 1

        else:
            run_cmd(console, savecfg)
            read1 = read_from_con(console)
            print(read1)
            print("Check prompt !!!! FAILURE level 1  OCCURRED")
            ct += 1
