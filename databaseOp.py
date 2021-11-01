# insert record in database

import cx_Oracle

def insertBal(NewAmt,pw):
    try:
        con=cx_Oracle.connect("system/dhamma1@localhost/orcl")
        cur=con.cursor()
        cur.execute("update ATM_user set balance=%d where password='%s'" %(NewAmt,pw))
        con.commit()
        if(cur.rowcount>0):
            print()
        else:
            print("Record Unable to Update......please try later")
    except cx_Oracle.DatabaseError as db:
        print("worning : ",db)
