from tkinter import *
import re
import threading
import time
from ericnuno import*
root = Tk()


def reset_button(command):
    inputValue = textBox.get("1.0", "end-1c")
    regex = re.findall(
        r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', inputValue)

    for r in regex:
        #print(r)
        #w = threading.Thread(target=ping_devices, args=(r,))
        
        #w.start()
    
        print('dones')
        x = threading.Thread(target=enter_command, args=(r, command))
        x.start()

#---ping function---


def ping_devices(ips):
    '''simple ping function that tests if we can connect into the 4500 device.'''
    
    chPing = ping(ips, n=3)
    print(chPing)
    if chPing == True:
        print('succesfully pinged to device ' + ips + ' continuing.')
   
    if chPing == False:
        print('connectivity issue, please try ' + ips + ' again.')


#---main function---


def enter_command(ips, command):
    try:
        ping_devices(ips)
        time.sleep(2)
        con, ch = ssh_connect(ips, 'administrator', '1q2w3e$R',
                              screenprint=True)
        psend(command + '\n', ch)
        pwait('status_tag=COMMAND COMPLETED', ch, tout=0, screenprint=True)
        print('process completed for ' + ips)
    except TimeoutError:
        print('timeout error: could not connect to the ip: ' +
              ips + ' please try again.')
    except ConnectionAbortedError:
        print('connection error: could not connect to the ip: ' +
              ips + ' please try again.')
    except paramiko.ssh_exception.NoValidConnectionsError:
        print('paramiko error: could not connect to the ip: ' +
              ips + ' please try again.')

#---Text Box---
textBox = Text(root, height=20, width=30)
textBox.grid(column=1, row=1, columnspan=2)
#---reset device---
resetBut = Button(root, height=2, width=16, text="Reset Server",
                  command=lambda: reset_button('power reset'))
resetBut.grid(column=1, row=2, sticky=W)
#---reset ilo button
iloOff = Button(root, height=2, width=16, text="Reset ILO",
                command=lambda: reset_button('reset /map1'))
iloOff.grid(column=1, row=3, sticky=W)
#---power on device---
powerOnBut = Button(root, height=2, width=16, text="Power on Device",
                    command=lambda: reset_button('power on'))
powerOnBut.grid(column=2, row=2, sticky=W)
#---power off device
powerOnBut = Button(root, height=2, width=16, text="Power off Device",
                    command=lambda: reset_button('power off hard'))
powerOnBut.grid(column=2, row=3, sticky=W)

mainloop()
