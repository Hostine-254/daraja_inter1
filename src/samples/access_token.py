import requests
from requests.auth import HTTPBasicAuth

from samples.keys import *

def generate_access_token():
    consumer_key = "6zziVX9V3e4S4sIsW6dwBVCXJ3knogpV"
    consumer_secret = "EC9601u33WISnXH9"
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.request("GET", api_URL , auth=HTTPBasicAuth(consumer_key, consumer_secret))

    #print(response.json()) #{'access_token': '4ncw7TO2e0jyQ2uTeAiNemwONPjd', 'expires_in': '3599'}

    json_response = response.json()
    my_access_token = json_response['access_token']
    
    return my_access_token