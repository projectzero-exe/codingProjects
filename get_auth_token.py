import requests
from requests.auth import HTTPBasicAuth

from dnac_config import USERNAME, PASSWORD, DNAC_IP, DNAC_PORT


def get_auth_token():
    """
    Building out Auth request. Using requests.post
    to make a call to the Auth Endpoint
    """

    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    r = requests.post(url, auth=HTTPBasicAuth(USERNAME, PASSWORD),
                      headers={'content-type': 'application/json'}, verify=False)
    token= r.json()['Token']
    print("Token retrieved from DNA Center is: {}".format(token))
    return token

if __name__ == "__main__":
    get_auth_token()


print('RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRAAAAAAAAAAAAAAAAAAWWWWWWWWWWWWWWWWWWWWWWRRRRRRRRRRRRRRRRR')