import cli

sn1 = cli.execute("show version | i ^Processor")
sn = sn1.split(" ")[-1]
print sn

#Performing Pre-Upgrade QC

print "\n* Performing Pre-Upgrade QC"
show_cmds = [
    "show clock",
    "term len 0",
    "Show version",
    "dir bootflash:",
    "dir stby-bootflash:",
    "dir harddisk:",
    "dir stby-harddisk:",
    "show inventory",
    "show platform",
    "show platform diag"
]

qc_str = [] 

for show_cmd in show_cmds:
    print "\n* Running command '{}'".format(show_cmd)
    qc_str.append(cli.execute(show_cmd))


upgr_qc = []

upgr_cmds = [
    "copy usb0:cbrsup-universalk9.16.12.01z1.SPA.bin bootflash:",
    "copy usb0:cbrsup-programmable_firmware.16.12.01z1.SPA.pkg harddisk:",
    "verify /md5 bootflash:cbrsup-universalk9.16.12.01z.SPA.bin d667307abe1b22402f433386c29f1684",
    "verify /md5 harddisk:cbrsup-programmable_firmware.16.12.01z.SPA.pkg efa72714534c123aa9c9c776b627b475",
    "request platform software package expand file bootflash:cbrsup-universalk9.16.12.01z.SPA.bin to bootflash:/XE-1612-1z/ wipe"

]

for cmd in upgr_cmds:
    print "\n* Running command '{}'".format(cmd)
    upgr_qc.append(cli.execute(cmd))



bootsys_cmds = [
    "no boot system",
    "boot system bootflash:/XE-1612-1z/packages.conf",
    "boot system bootflash:/cbrsup-universalk9.16.12.01z.SPA.bin"
]


x = cli.configure(bootsys_cmds)


cli.executep("write mem")

with open("/bootflash/{}.log".format(sn), "a") as f:
    for i in range(len(qc_str)):
        f.write("#############START OF SEGMENT##############\n")
        f.write("")
        f.write(qc_str[i])
        f.write("")
        f.write("#############END OF SEGMENT##############\n")

with open("/bootflash/{}.log".format(sn), "a") as f:
    for i in range(len(upgr_qc)):
        f.write("#############START OF SEGMENT##############\n")
        f.write("")
        f.write(upgr_qc[i])
        f.write("")
        f.write("#############END OF SEGMENT##############\n")

with open("/bootflash/{}.log".format(sn), "a") as f:
        f.write("#############START OF SEGMENT##############\n")
        f.write("")
        f.write(x)
        f.write("")
        f.write("#############END OF SEGMENT##############\n")

cli.clip("copy bootflash:{}.log usb0: ; \n".format(sn))

