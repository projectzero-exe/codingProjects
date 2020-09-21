import TOR_JP

console = TOR_JP.open_con()

#TOR_JP.chk_poap_and_initconfig_dialog(console)

#TOR_JP.chk_poap_pass(console)

TOR_JP.access_switch(console)
#
TOR_JP.run_cmd(console, 'term len 0')
#
TOR_JP.run_cmd(console,'show version', 6)

TOR_JP.run_cmd(console,'copy usb1:sf_leaf_a_config_LACP.cfg startup-config', 10)

TOR_JP.run_cmd(console,'reload', 4)

TOR_JP.run_cmd(console,'y', 6)
#


output = TOR_JP.read_from_con(console)
print(output)



