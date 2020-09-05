import requests
from requests.auth import HTTPBasicAuth
import get_auth_token
from dnac_config import USERNAME, PASSWORD
import pprint

def get_device_list():
    token = get_auth_token()
    url = 'https://sandboxdnac.cisco.com/api/v1/network-device'
    hdr = {'x-auth-token': token, 'content-type': 'application/json'}
    r = requests.get(url, headers=hdr, verify=False)
    device_list = r.json()
    #print(device_list)
    pprint.pprint(device_list)

def get_auth_token():
    """
    Building out Auth request. Using requests.post
    to make a call to the Auth Endpoint
    """

    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    r = requests.post(url, auth=HTTPBasicAuth(USERNAME, PASSWORD),
                      headers={'content-type': 'application/json'}, verify=False)
    token = r.json()['Token']
    print("Token retrieved from DNA Center is: {}".format(token))
    return token

if __name__ == '__main__':
    get_device_list()


print("@@@@@@@@@@@@@@@@@@@@@@@@@")