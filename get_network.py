import requests
from dnac_config import IP2
from get_auth_token import get_auth_token
from pprint import pprint


def get_device_list():

    token = get_auth_token()

    #params = {'response': 'family;routers', 'fullText': 'true'}
    hdr = {'x-auth-token': token, 'content-type': 'application/json'}
    r = requests.get(IP2, headers=hdr, verify=False)
    #pprint(r.json()['response'])
    print_device_list(r.json())


def print_device_list(device_json):
    print(f"{'HostName':42}{'MgmtIpAddress':17}{'SerialNumber':16}{'PlatformId':18}"
          f"{'SoftwareVersion':18}{'Role':16}{'UpTime':15}")
    print(f'{"-" * 147}')
    for device in device_json['response']:
        print(f"{device['hostname']:42}{device['managementIpAddress']:17}{device['serialNumber']:16}"
              f"{device['platformId']:18}{device['softwareVersion']:18}{device['role']:16}{device['upTime']:15}")

    print(f'{"-" * 147}')


if __name__ == '__main__':
    get_device_list()