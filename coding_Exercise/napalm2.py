from napalm import get_network_driver

driver = get_network_driver('nxos')
device = driver('10.233.30.3', 'admin', 'WWTwwt1!')
device.open()


device.close
