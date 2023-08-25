

def mobitech(voucher_detail,ph_nmber):
       
       import requests

       import simplejson as json
        
       send_number = ''

       msg_to_send = ''
       
       if voucher_detail[0] == 0:
              send_number ='254722888543'
              msg_to_send =voucher_detail[1]
       if voucher_detail[1] == 1:
              send_number =ph_nmber
              voucher_msg = str(voucher_detail[0])
              msg_to_send = 'Voucher password: %s' % (voucher_msg)
       else:
              pass

       url = 'https://api.mobitechtechnologies.com/sms/sendsms'

       payload = {
          "mobile": send_number,
          "response_type": "json",
          "sender_name": "23107",
          "service_id": 0,
          "message": msg_to_send + ' \n \t\t\tNetView <Simple!, Cheap!, Reliable!'
        }

       headers = {
             'h_api_key': '8f6a769926b904415f51e8baaecd3e84da74ee5e6669a6d076bd627b63c19864',
              'Content-Type': 'application/json'
            }

       response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

       print(response.text.encode('utf8'))

#mobitech(['1234',1],'254722888543')