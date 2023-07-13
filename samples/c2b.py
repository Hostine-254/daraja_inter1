import requests

import simplejson as json

from access_token import generate_access_token
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