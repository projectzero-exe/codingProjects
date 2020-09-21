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
    print(type(todos))
    print(todos)
    todos['response'] = [dict(hostname=k1['hostname'],managementIpAddress=k1['managementIpAddress'])
                         for k1 in todos['response']] #this way i can call on specific key values return from the response

    pprint(type(todos))
    pprint(todos)



if __name__ == '__main__':
    get_device_list()