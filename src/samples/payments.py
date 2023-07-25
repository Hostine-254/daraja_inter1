import requests
import simplejson as jsop
import json
from requests.auth import HTTPBasicAuth
import base64
from datetime import datetime
from json import JSONDecodeError


def generate_access_token():
    consumer_key = "XeCcC6RpPy5af5nb7AGG60k3t2wqcmkg"
    consumer_secret = "pTikngLOEedhvbYK"
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    try:
        response = requests.request("GET", api_URL , auth=HTTPBasicAuth(consumer_key, consumer_secret))
    except:
        response = requests.request("GET", api_URL , auth=HTTPBasicAuth(consumer_key, consumer_secret),verify=False)

    #print(response.text) #{'access_token': '4ncw7TO2e0jyQ2uTeAiNemwONPjd', 'expires_in': '3599'}
    json_response = response.json()

    my_access_token = json_response['access_token']
        
    return my_access_token


def lipa_na_mpesa(customer_number, customer_amount):

    access_token = generate_access_token()
    
    formatted_time = get_timestamp()
    decoded_password = generate_password(formatted_time)

    api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest?format=json' 

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
        "AccountReference": "Netview payment",
        "TransactionDesc": "Payment of development", 
      }


    response = requests.request("POST", api_url , headers = headers, data = json.dumps(payload))
    print(response.text.encode('utf8'))


def generate_password(formatted_time):
    business_ShortCode = "174379"
    lipa_na_mpesa_passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"

    data_to_encode = business_ShortCode + lipa_na_mpesa_passkey + formatted_time
    encode_string = base64.b64encode(data_to_encode.encode())
    #print(encode_string) b'MTc0Mzc5MjAyMzA2MjAyMzQ4MTE='

    decoded_password = encode_string.decode("utf-8")
    #print(decoded_password)
    return decoded_password



def get_timestamp():
    #print(datetime.now()) #2023-06-20 23:29:58.157425 required format(20230620232956)
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
    #print(formatted_time)
    return formatted_time

#lipa_na_mpesa("254722888543",2)
generate_access_token()