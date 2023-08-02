

def mobitech(voucher_detail,ph_nmber='0722xxxxxx'):
       
       import requests

       import simplejson as json
        
       send_number = ''

       msg_to_send = ''
       
       if voucher_detail[0] == 0:
              send_number ='254722888543'
              msg_to_send =voucher_detail[1]
       elif voucher_detail[1] == 1:
              send_number =ph_nmber
              msg_to_send = 'login: %s  password: %s' % (voucher_detail[0][0], voucher_detail[0][1])
       else:
              pass

       url = 'https://api.mobitechtechnologies.com/sms/sendsms'

       payload = {
          "mobile": send_number,
          "response_type": "json",
          "sender_name": "23107",
          "service_id": 0,
          "message": msg_to_send + ' \n \t\t\tNetView <Sample!, Cheap!, Reliable!'
        }

       headers = {
             'h_api_key': '8f6a769926b904415f51e8baaecd3e84da74ee5e6669a6d076bd627b63c19864',
              'Content-Type': 'application/json'
            }

       response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

       print(response.text.encode('utf8'))

#mobitech(254722888543)