import requests
from dnac_config import IP2
from get_auth_token import get_auth_token
from pprint import pprint


def get_device_list():

    token = get_auth_token()

    #params = {'response': 'family;routers', 'fullText': 'true'}
    hdr = {'x-auth-token': token, 'content-type': 'application/json'}
    r = requests.get(IP2, headers=hdr, verify=False)
    pprint(r.json()['response'])
    print_device_list(r.json())


def print_device_list(device_json):
    print(f"{'HostName':42}{'MgmtIpAddress':17}{'SerialNumber':16}{'PlatformId':18}{'SoftwareVersion':18}{'Role':16}{'UpTime':15}")
    print(f'{"-" * 147}')
    for device in device_json['response']:
        print(f"{device['hostname']:42}{device['managementIpAddress']:17}{device['serialNumber']:16}{device['platformId']:18}{device['softwareVersion']:18}{device['role']:16}{device['upTime']:15}")

    print(f'{"-" * 147}')
    # print(type(todos))
    # print(todos)
    # todos['response'] = [dict(hostname=k1['hostname'],managementIpAddress=k1['managementIpAddress'], )
    #                      for k1 in todos['response']] #this way i can call on specific key values return from the response
    # # data = json.dumps(todos)
    # pprint(type(todos))
    # pprint(todos)

if __name__ == '__main__':
    get_device_list()