# create ATM table in oracle database

import cx_Oracle

try:
    con=cx_Oracle.connect("system/dhamma1@localhost/orcl")
    cur=con.cursor()
    cur.execute("create table ATM_user(balance number(30), username varchar(20), password varchar(20))")
    print("Table Created Successfully")
except cx_Oracle.DatabaseError as db:
    print(" worning :",db)
