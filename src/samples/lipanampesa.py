import requests
import simplejson as json

from access_token import generate_access_token
from encode import generate_password
from utils import get_timestamp
import keys


def lipa_na_mpesa(): 
    
    formatted_time = get_timestamp()
    decoded_password = generate_password(formatted_time)

    access_token = generate_access_token()

    api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest' 

    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer %s' % access_token,
    }

    payload = {
        "BusinessShortCode": keys.business_ShortCode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": keys.phone_number,
        "PartyB": keys.business_ShortCode,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "Netview Fix",
        "TransactionDesc": "Payment of development", 
      }

    response = requests.request("POST", api_url , headers = headers, data = json.dumps(payload))
    print(response.text.encode('utf8'))

lipa_na_mpesa()