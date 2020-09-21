import requests
from requests.auth import HTTPBasicAuth

from dnac_config import UN, PW, IP

requests.urllib3.disable_warnings()


def get_auth_token():
    """
    Building out Auth request. Using requests.post
    to make a call to the Auth Endpoint
    """

    url = IP
    r = requests.post(url, auth=HTTPBasicAuth(UN, PW),
                      headers={'content-type': 'application/json'}, verify=False)
    token = r.json()['Token']
    #print(f"Token retrieved from DNA Center is: {token}")
    return token


if __name__ == "__main__":
    get_auth_token()
