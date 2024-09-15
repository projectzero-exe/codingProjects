import threading
#from datetime import datetime
import initConsole_cfg
import cmd_ls
"""Work in progress. Will leverage initConsole library to perform initial configuration via serial console and distributed via Multithreading"""
def multiprocessing(con):
    console = initConsole_cfg.open_con(con)

    boot_config = [
        "conf t", "config-register 0x2102",
        "no boot sys", "boot system bootflash:ISSU/packages.conf",
        "end", "wr",
    ]
    sla1_on = [
        "conf t", "ip sla sch 1 start now"
    ]
    sla2_on = [
        "conf t", "ip sla sch 2 start now"
    ]

    sla1_off = [
        "conf t", "no ip sla sch 1 start now"
    ]

    sla2_off = [
        "conf t", "no ip sla sch 2 start now"
    ]



    initConsole_cfg.run_cmd(console)
    initConsole_cfg.run_cmd(console, 'boot usb0:ncs4202-universalk9_npe.16.06.08vS.SPA.bin', 480)

    i = 0
    while i < 21:
        initConsole_cfg.run_cmd(console, sleep=20)
        output = initConsole_cfg.read_from_con(console)
        print(output)
        i += 1
        print(i)
    i = 0
    while i < 6:
        initConsole_cfg.run_cmd(console, sleep=3)
        output = initConsole_cfg.read_from_con(console)
        print(output)
        output1 = output.split()
        print(output1)
        print(i)
        if "initial" in output1 and "configuration" in output1:
            initConsole_cfg.run_cmd(console, "no\n", 2)
            i += 1

        elif "autoinstall?" in output1:
            initConsole_cfg.run_cmd(console, "\n\n", sleep=2)
            i += 1
        else: i += 1


    initConsole_cfg.run_cmd(console, sleep=30)
    initConsole_cfg.run_cmd(console)
    initConsole_cfg.run_cmd(console)
    initConsole_cfg.parsercheck(console, sleep=2)
    initConsole_cfg.run_cmd(console, 'mkdir bootflash:ISSU')
    initConsole_cfg.run_cmd(console)
    initConsole_cfg.run_cmd(console, 'copy usb0:ncs4202-universalk9_npe.16.06.08vS.SPA.bin bootflash:ISSU/', sleep=60)
    initConsole_cfg.run_cmd(console)
    initConsole_cfg.parsercheck(console, sleep=3)
    initConsole_cfg.run_cmd(console, 'dir bootflash:ISSU', 3)
    print(initConsole_cfg.read_from_con(console))
    initConsole_cfg.run_cmd(console, 'request platform software package expand file bootflash:ISSU/ncs4202-universalk9_npe.16.06.08vS.SPA.bin', sleep=240)
    initConsole_cfg.parsercheck(console, sleep=2)
    initConsole_cfg.run_list_cmd(console, cmd_ls.show_quality)
    initConsole_cfg.run_cmd(console, "wr", 10)
    initConsole_cfg.parsercheck(console)
    r = initConsole_cfg.showplattoDict(console)
    x = r[6]["Firmware Ver"]
    y = r[7]["Firmware Ver"]
    if x != "15.6(24r)S" and y != "15.6(24r)S":
        initConsole_cfg.run_cmd(console, "copy usb0:NCS4202_15_6_24r_s_rommon.pkg bootflash:", 5)
        initConsole_cfg.parsercheck(console, sleep=3)
        initConsole_cfg.run_cmd(console, "upgrade rom-monitor filename bootflash:NCS4202_15_6_24r_s_rommon.pkg all", 75)
    initConsole_cfg.parsercheck(console, sleep=3)
    initConsole_cfg.run_list_cmd(console, boot_config)
    initConsole_cfg.parsercheck(console, sleep=3)
    initConsole_cfg.run_cmd(console, "show boot")
    initConsole_cfg.reloadsequence(console, savecfg="y\n", sleep=500)  # savecfg parameter needs to be specified either yes or no. prompt is asking you save configs
    initConsole_cfg.parsercheck(console, sleep=2)
    initConsole_cfg.run_cmd(console, "copy usb0:4202ipc.cfg running-config", 1)
    initConsole_cfg.run_cmd(console, "\n\n", 2)
    initConsole_cfg.run_list_cmd(console, sla1_on, 2)

    # """Creating a file to log QC while extracting the serial number from the
    # device and use it as its naming convention"""
    # now = datetime.now()
    # year = now.year
    # month = now.month
    # day = now.day
    # # creating the backup filename (hostname_date_backup.txt)
    # filename = f"{oP}_{year}_{month}_{day}_QC.txt"
    # # writing the backup to the file
    # log = open(filename, 'wt')
    # log.write(output)
    # print(f'Backup of {oP} completed successfully')
    # print('#' * 30)
    # log.close()


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

for consoles in consoles_iter:
    """creating a thread for each target that executes the multiprocessing function"""
    th = threading.Thread(target=multiprocessing, args=(consoles,))
    threads.append(th)
"""starting the threads"""
for th in threads:
    th.start()
"""waiting for the threads to finish"""
for th in threads:
    th.join()
