import requests
from requests.auth import HTTPBasicAuth
from dnac_creds import IP, PW, UN
import get_auth_token
import json

def get_device_info():
    """Building a function to retrieve a list of devices registered to the DNA center; Using request method 'Get'"""

    token = get_auth_token
    hdr = {'x-auth-token': token, 'content-type': 'application/json'}

    url = "https://sandboxdnac.cisco.com/api/v1/network-device"
    print(url)
    response = requests.get(url, headers=hdr)
    print(response.json())
    # device_list = response.json()
    # json = device_list.load()
    # print(json)