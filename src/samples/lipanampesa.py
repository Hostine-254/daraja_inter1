import requests
import simplejson as json

from samples.access_token import generate_access_token
from samples.encode import generate_password
from samples.utils import get_timestamp
from samples.keys import *


def lipa_na_mpesa(customer_number, customer_amount): 
    
    access_token = generate_access_token()
    
    formatted_time = get_timestamp()
    decoded_password = generate_password(formatted_time)

    api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest' 

    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer %s' % access_token,
    }

    payload = {
        "BusinessShortCode": "174379",
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": customer_amount,
        "PartyA": customer_number,
        "PartyB": "174379",
        "PhoneNumber": customer_number,
        "CallBackURL": "https://immense-basin-10854-a03a17f67646.herokuapp.com/api/payments/lnm/",
        "AccountReference": "django payment",
        "TransactionDesc": "Payment of development", 
      }

    response = requests.request("POST", api_url , headers = headers, data = json.dumps(payload))
    #print(response.text.encode('utf8'))