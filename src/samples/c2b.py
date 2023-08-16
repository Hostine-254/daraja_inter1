import requests

import simplejson as json

from samples.access_token import generate_access_token
import keys

my_access_token =generate_access_token()
def register_url():
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer %s' % my_access_token
    }

    payload = {
        "ShortCode": keys.shortcode ,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://fullstackdjango.com/confirmation",
        "ValidationURL": "https://fullstackdjango.com/validation",
    }

    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl', headers = headers, data = json.dumps(payload))
    print(response.text.encode('utf8'))

register_url()

def simulate_c2b_transaction():
    my_access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    
    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = {
        "ShortCode": keys.shortcode,
        "CommandID": "CustomerBuyGoodsOnline",
        "Amount": 2,
        "Msisdn": "254708374149",
        "BillRefNumber": "12345678",

    }
    response =  requests.request("POST",api_url , headers = headers, data = json.dumps(request))
    print(response.text)