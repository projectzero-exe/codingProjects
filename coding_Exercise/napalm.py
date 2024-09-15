
from napalm import get_network_driver
import json
import urllib3



driver = get_network_driver('nxos')
#optional_args = {'secret': 'cisco'} #cisco is in the "enable password"
ios = driver('10.233.30.3', 'admin', 'WWTwwt1!')
ios.open()
#start code
ips = '10.233.30.1', '10.233.30.3'
for output in ips:
    ios.ping(output)
#output = ios.ping('10.233.30.1')
dump = json.dumps(output, sort_keys=True, indent=4)
with open('ping_table.txt', 'w') as f:
       f.write(dump)
ping_j = open("ping_table.txt")

read_ping = ping_j.read()

success_ping = json.loads(read_ping)

print(success_ping)


#end your code
ios.close()
