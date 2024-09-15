import requests
from requests.auth import HTTPBasicAuth
from dnac_creds import IP, PW, UN


"""Defining a function to Auth request. 
Leveraging request method 'post' to make a call Auth endpoint"""

requests.urllib3.disable_warnings() #Disables "InsecureRequestWarning" warning message

def get_token():

    hdr = {'content-type': 'application/json'}
    response = requests.post(IP, auth=HTTPBasicAuth(UN, PW), headers=hdr, verify=False)
    token = response.json()['Token']
    print(f"Token retrieved: {token}")
    return token

if __name__ == "__main__":
    get_token()