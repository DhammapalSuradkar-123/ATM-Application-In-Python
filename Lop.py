# Login Operations
import cx_Oracle
import databaseOp

# Deposite Section
def deposite(pw):
    try:
        con=cx_Oracle.connect("system/dhamma1@localhost/orcl")
        cur=con.cursor()
        cur.execute("select balance from ATM_user where password='%s'" %pw)
        while(True):
            bal=cur.fetchone()
            if(bal==None):
                break
            else:
                for val in bal:
                    d1=val
        try:
            d2=int(input("Enter Ammount For Diposite : "))
            if(d2<=0):
                print("-"*40)
                print("worning : Please Enter valid Ammount")
            else:
                d=d1+d2
                databaseOp.insertBal(d,pw)
                print("*"*60)
                print("Your Account xxxxx1234 has been creadited with [ %d INR ].\nAvailabel Bal. [ %d INR ]." %(d2,d))
        except ValueError:
            print("worning : Do Not Enter String Data/Special Symbol/Alpha-Numeric Data")
    except cx_Oracle.DatabaseError as db:
        print("worning : ",db)

# Withdrow Section
def withdrow(pw):
    try:
        con=cx_Oracle.connect("system/dhamma1@localhost/orcl")
        cur=con.cursor()
        cur.execute("select balance from ATM_user where password='%s'" %pw)
        while(True):
            bal=cur.fetchone()
            if(bal==None):
                break
            else:
                for val in bal:
                    d1=val
        try:
            d2=int(input("Enter Ammount For withdrow : "))
            if(d2>d1):
                print("*"*30)
                print("worning : Your Account have Insufficient Balance")
            else:
                d=d1-d2
                databaseOp.insertBal(d,pw)
                print("*"*60)
                print("Your Account xxxxx1234 Debited with [ %d INR ].\nAvailabel Bal. [ %d INR ]." %(d2,d))                
        except ValueError:
            print("-"*30)
            print("Worning : Do not Enter String Data/Special Symbol/Alpha-Numeric Data")
    except cx_Oracle.DatabaseError as db:
        print("worning : ",db)

# Balance Inc Section
def BalInc(pw):
    try:
        con=cx_Oracle.connect("system/dhamma1@localhost/orcl")
        cur=con.cursor()
        cur.execute("select balance from ATM_user where password='%s'" %pw)
        while(True):
            bal=cur.fetchone()
            if(bal==None):
                break
            else:
                for val in bal:
                    d1=val
        print("*"*60)
        print("Available Balance In A/C xxxxx1234 is [ %d INR ]." %d1)
    except cx_Oracle.DatabaseError as db:
        print("worning : ",db)
