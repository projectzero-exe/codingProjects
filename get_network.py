import requests
from dnac_config import IP2
from get_auth_token import get_auth_token
from pprint import pprint
import json

def get_device_list():

    token = get_auth_token()


    hdr = {'x-auth-token': token, 'content-type': 'application/json'}
    r = requests.get(IP2, headers=hdr, verify=False)
    todos = r.json()
    print_device_list(todos)

def print_device_list(device_json):
    print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
              format("hostname", "mgmt IP", "serial", "platformId", "SW Version", "role", "Uptime"))
    for device in device_json['response']:
            uptime = "N/A" if device['upTime'] is None else device['upTime']
            if device['serialNumber'] is not None and "," in device['serialNumber']:
                serialPlatformList = zip(device['serialNumber'].split(","), device['platformId'].split(","))
            else:
                serialPlatformList = [(device['serialNumber'], device['platformId'])]
            for (serialNumber, platformId) in serialPlatformList:
                print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
                      format(device['hostname'],
                             device['managementIpAddress'],
                             serialNumber,
                             platformId,
                             device['softwareVersion'],
                             device['role'], uptime))

    # print(type(todos))
    # print(todos)
    # todos['response'] = [dict(hostname=k1['hostname'],managementIpAddress=k1['managementIpAddress'], )
    #                      for k1 in todos['response']] #this way i can call on specific key values return from the response
    # # data = json.dumps(todos)
    # pprint(type(todos))
    # pprint(todos)

if __name__ == '__main__':
    get_device_list()