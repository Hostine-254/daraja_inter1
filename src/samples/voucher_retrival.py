
import shelve


  
def get_Voucher(amount,locale):
    voucher_available = 1
    if amount == 2 and locale=="Thika":
        with shelve.open('dbms/db_Th_Day') as db:
           #db.update(data)
           msg = "Shs 20 Vouchers are almost depleted REF: Thika"
           ret = voucher_logic(db)
           
           #print(dict(db))
           if ret == 0:
              return (ret,msg)
              #print("Shs 20 Vouchers are almost depleted")
           else:
              return (ret,voucher_available)
    elif amount == 100 and locale=="Thika":
        with shelve.open('dbms/db_Th_Week') as db:
           #db.update(data)
           msg = "Shs 100 Vouchers are almost depleted REF: Thika"
           ret = voucher_logic(db)
           if ret == 0:
              return (ret,msg)
               #print("Shs 100 Vouchers are almost depleted")
           else:
              return (ret,voucher_available)
    elif amount ==320 and locale=="Thika":
        with shelve.open('dbms/db_Th_Month') as db:
           #db.update(data)
           msg = "Shs 320 Vouchers are almost depleted REF: Thika"
           ret = voucher_logic(db)
           if ret == 0:
               return (ret,msg)
               #print("Shs 300 Vouchers are almost depleted")
           else:
               return (ret,voucher_available)
           
    #code for Nairobi

    if amount == 2 and locale=="Nairobi":
        with shelve.open('dbms/db_Nb_Day') as db:
           #db.update(data)
           msg = "Shs 20 Vouchers are almost depleted REF: Nai"
           ret = voucher_logic(db)
           
           #print(dict(db))
           if ret == 0:
              return (ret,msg)
              #print("Shs 20 Vouchers are almost depleted")
           else:
              return (ret,voucher_available)
    elif amount == 100 and locale=="Nairobi":
        with shelve.open('dbms/db_Nb_Week') as db:
           #db.update(data)
           msg = "Shs 100 Vouchers are almost depleted REF: Nai"
           ret = voucher_logic(db)
           if ret == 0:
              return (ret,msg)
               #print("Shs 100 Vouchers are almost depleted")
           else:
              return (ret,voucher_available)
    elif amount ==320 and locale=="Nairobi":
        with shelve.open('dbms/db_Nb_Month') as db:
           #db.update(data)
           msg = "Shs 320 Vouchers are almost depleted REF: Nai"
           ret = voucher_logic(db)
           if ret == 0:
               return (ret,msg)
               #print("Shs 300 Vouchers are almost depleted")
           else:
               return (ret,voucher_available)

    else:
       pass

           
def voucher_logic(db):
    count = len(db.keys())
    if bool(db) and count >= 3:
      voucher = db.popitem()
      #login =voucher[0]
      password = voucher[1]

      print('password: %s' % (password))
      return (password)
    else:
      return 0
    

def view_logs_voucher(locale):
    data = {}
    if locale == "Thika":
       with shelve.open('dbms/db_Th_Logs') as db:
          data = dict(db)
       return data
    elif locale == "Nairobi":
       with shelve.open('dbms/db_Nb_Logs') as db:
          data = dict(db)
       return data
    else:
       pass
          