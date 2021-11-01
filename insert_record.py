# insert first record
import cx_Oracle

try:
    con=cx_Oracle.connect("system/dhamma1@localhost/orcl")
    cur=con.cursor()
    cur.execute("insert into ATM_user values(1, 1000, 'Tony Stark', 'ts')")
    con.commit()
    if(cur.rowcount>0):
        print("Data Inserted Successfully")
    else:
        print("Data Unable to Insert......Please try later")
except cx_Oracle.DatabaseError as db:
    print("worning : ",db)
