
import shelve


  
def get_Voucher(amount):
    voucher_available = 1
    if amount == 2:
        with shelve.open('dbms/db_Th_Day') as db:
           #db.update(data)
           msg = "Shs 20 Vouchers are almost depleted"
           ret = voucher_logic(db)
           
           #print(dict(db))
           if ret == 0:
              return (ret,msg)
              #print("Shs 20 Vouchers are almost depleted")
           else:
              return (ret,voucher_available)
    elif amount == 100:
        with shelve.open('dbms/db_Th_Week') as db:
           #db.update(data)
           msg = "Shs 100 Vouchers are almost depleted"
           ret = voucher_logic(db)
           if ret == 0:
              return (ret,msg)
               #print("Shs 100 Vouchers are almost depleted")
           else:
              return (ret,voucher_available)
    elif amount ==320:
        with shelve.open('dbms/db_Th_Month') as db:
           #db.update(data)
           msg = "Shs 320 Vouchers are almost depleted"
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
      login =voucher[0]
      password = voucher[1]

      print('login: %s password: %s' % (login,password))
      return (login,password)
    else:
      return 0
    