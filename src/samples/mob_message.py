

def mobitech(voucher_detail,ph_nmber,locale="nil"):
       
       import requests

       import simplejson as json
       loc = locale.title()
       send_number = ''

       msg_to_send = ''
       
       if voucher_detail[0] == 0:
              send_number ='254722888543'
              msg_to_send =voucher_detail[1]
       if voucher_detail[1] == 1:
              send_number = ph_nmber
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

       save_logs(voucher_detail,ph_nmber,loc)

       print(response.text.encode('utf8'))

#mobitech(['1234',1],'254722888543')
def save_logs(voucher_det,ph_no,locale):
       import shelve
       try:
              if voucher_det[1] == 1:
                     password = str(voucher_det[0])
                     data = {password:ph_no}
                     if locale == "Thika" :
                            with shelve.open('dbms/db_Th_Logs') as db:
                                   db.update(data)
                     elif locale == "Nairobi" :
                            with shelve.open('dbms/db_Nb_Logs') as db:
                                   db.update(data)
                     else:
                            pass
                     print("Called this function")
              else:
                     pass
       except:
              pass
