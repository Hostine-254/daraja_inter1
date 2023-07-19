
def mobitech(phone_number):
       import requests

       import simplejson as json

       url = 'https://api.mobitechtechnologies.com/sms/sendsms'

       payload = {
          "mobile": phone_number,
          "response_type": "json",
          "sender_name": "23107",
          "service_id": 0,
          "message": "niaje max ni Hostine"
        }

       headers = {
             'h_api_key': '8f6a769926b904415f51e8baaecd3e84da74ee5e6669a6d076bd627b63c19864',
              'Content-Type': 'application/json'
            }

       response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

       print(response.text.encode('utf8'))

mobitech(254722888543)