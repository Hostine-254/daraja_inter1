

import shelve

def value_extract(locale,span,data):
    if locale =="thika":
        if span == "hour":
            with shelve.open('dbms/db_Th_Hour') as db:
                pass
        if span == "day":
            with shelve.open('dbms/db_Th_Day') as db:
                db.update(data)
        if span == "week":
            with shelve.open('dbms/db_Th_Week') as db:
                db.update(data)
        if span == "month":
            with shelve.open('dbms/db_Th_Month') as db:
                db.update(data)

    if locale =="nairobi":
        if span == "hour":
            with shelve.open('dbms/db_Nb_Hour') as db:
                pass
        if span == "day":
            with shelve.open('dbms/db_Nb_Day') as db:
                db.update(data)
        if span == "week":
            with shelve.open('dbms/db_Nb_Week') as db:
                db.update(data)
        if span == "month":
            with shelve.open('dbms/db_Nb_Month') as db:
                db.update(data)
    else:pass

def voucher_delete(locale,span):
    if locale =="thika":
        if span == "hour":
            with shelve.open('dbms/db_Th_Hour') as db:
                pass
        if span == "day":
            with shelve.open('dbms/db_Th_Day') as db:
                for key in db:
                    del db[key]
                return 1
        if span == "week":
            with shelve.open('dbms/db_Th_Week') as db:
                for key in db:
                    del db[key]
                return 1
        if span == "month":
            with shelve.open('dbms/db_Th_Month') as db:
                for key in db:
                    del db[key]
                return 1

    if locale =="nairobi":
        if span == "hour":
            with shelve.open('dbms/db_Nb_Hour') as db:
                pass
        if span == "day":
            with shelve.open('dbms/db_Nb_Day') as db:
                for key in db:
                    del db[key]
                return 1
        if span == "week":
            with shelve.open('dbms/db_Nb_Week') as db:
                for key in db:
                    del db[key]
                return 1
        if span == "month":
            with shelve.open('dbms/db_Nb_Month') as db:
                for key in db:
                    del db[key]
                return 1
        else:return 0
    else:return 0