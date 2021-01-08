import initial_nexus3k9kp2
from datetime import datetime
import threading


def multiprocessing(consoles, baudrate):
    console = initial_nexus3k9kp2.open_con(consoles, baudrate)

    initial_nexus3k9kp2.chk_poap_and_initconfig_dialog(console, 4)
    initial_nexus3k9kp2.access_switch(console, 4)
    initial_nexus3k9kp2.run_cmd(console, 'term len 0')
    initial_nexus3k9kp2.run_cmd(console, 'show inventory')
    initial_nexus3k9kp2.run_cmd(console, 'delete /r /f flash:c3560*', 4)
    initial_nexus3k9kp2.run_cmd(console, '\r\n', 30)
    initial_nexus3k9kp2.run_cmd(console, '\r\n', 4)
    initial_nexus3k9kp2.run_cmd(console, 'copy usbflash0:c3560cx-universalk9-mz.152-4.E6.bin flash:', 4)
    initial_nexus3k9kp2.run_cmd(console, '\r\n', 4)
    initial_nexus3k9kp2.run_cmd(console, '\r\n', 300)
    initial_nexus3k9kp2.run_cmd(console, 'conf t', 4)
    initial_nexus3k9kp2.run_cmd(console, 'no boot system', 4)
    initial_nexus3k9kp2.run_cmd(console, 'boot system flash:c3560cx-universalk9-mz.152-4.E6.bin', 4)
    initial_nexus3k9kp2.run_cmd(console, 'end', 4)
    initial_nexus3k9kp2.run_cmd(console, 'wr', 6)
    initial_nexus3k9kp2.run_cmd(console, 'reload')
    initial_nexus3k9kp2.run_cmd(console, '\r\n', 330)
    initial_nexus3k9kp2.run_cmd(console, '\r\n', 4)
    initial_nexus3k9kp2.access_switch(console, 4)
    initial_nexus3k9kp2.chk_poap_and_initconfig_dialog(console, 2)
    initial_nexus3k9kp2.access_switch(console, 2)
    initial_nexus3k9kp2.run_cmd(console, 'term len 0')
    initial_nexus3k9kp2.run_cmd(console, 'show inventory')
    initial_nexus3k9kp2.run_cmd(console, 'show version', 3)
    initial_nexus3k9kp2.run_cmd(console, 'dir', 3)
    initial_nexus3k9kp2.run_cmd(console, 'show boot', 3)
    initial_nexus3k9kp2.run_cmd(console)

    output = initial_nexus3k9kp2.read_from_con(console)
    # output1 = output.splitlines() #Split a string into a list where each line is a list item
    output1 = output.split()  # Split a string into a list where each word is a list item
    print(type(output1))
    print(output1)
    """Using la,bda expression to surgically extract serial numbers from the list output"""
    oP1 = list(filter(lambda a: 'FOC' in a, output1))
    oP = oP1[0]
    print(oP)

    """Creating a file to log QC while extracting the serial number from the 
    device and use it as its naming convention"""
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    # creating the backup filename (hostname_date_backup.txt)
    filename = f"{oP}_{year}_{month}_{day}_QC.txt"
    # writing the backup to the file
    log = open(filename, 'wt')
    log.write(output)
    print(f'Backup of {oP} completed successfully')
    print('#' * 30)
    log.close()


"""creating variables to get put into a list"""
# console1 = "COM3"
# console2 = "COM4"
# console3 = "COM7"
# console4 = "COM8"
# console5 = "COM9"
# console6 = "COM10"
# console7 = "COM11"
# console8 = "COM12"
# console9 = "COM13"
# console10 = "COM14"
# console11 = "COM15"
# console12 = "COM16"
# console13 = "COM17"
# console14 = "COM18"
# console15 = "COM19"
# console16 = "COM20"

"""creating a list (of devices)"""

max_ports = int(input("How many console ports do you have operational? "))

consoles_iter = []

for port_n in range(max_ports):
    consoles_iter.append("COM" + input("Enter COM number to utilize: "))

"""creating an empty list (it will store the threads)"""
threads = list()

for consoles in console_iter:
    """creating a thread for each target that executes the multiprocessing function"""
    th = threading.Thread(target=multiprocessing, args=(consoles,))
    threads.append(th)
"""starting the threads"""
for th in threads:
    th.start()
"""waiting for the threads to finish"""
for th in threads:
    th.join()
