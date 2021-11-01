# ATM Operations
import databaseOp
import cx_Oracle
from login_menu import Lmenu
import random
from playsound import playsound

try:
    con=cx_Oracle.connect("system/dhamma1@localhost/orcl")
    cur=con.cursor()
    cur.execute("select balance from ATM_user")
    while(True):
        bal=cur.fetchone()
        if(bal==None):
            break
        else:
            for val in bal:
                d1=val

    # Login Section
    def login():
        try:
            username=input("Enter Username : ")
            pin=int(input("Enter pin number : "))
        except ValueError:
            print("-"*40)
            print("worning : Do not used string data/special symbol/alpha-numeric data")
        else:
            try:
                cur.execute("select username,pin,password from ATM_user where username like '%s'" %username)
                while(True):
                    e=cur.fetchone()
                    if(e==None):
                        break
                    else:
                        un=e[0]
                        up=e[1]
                        pw=e[2]
                if(username==un and pin==up):
                    print("-"*50)
                    print("\t Login Successful")
                    Lmenu(pw)
                else:
                    print("-"*30)
                    print("Worning : Incorrect UserName and pin")
            except UnboundLocalError:
                print("-"*30)
                print("worning : Record Not Found")

    # Create New Account
    def NewAcc():
        try:
            print("*"*50)
            print("\tCreate New Account")
            print("*"*50)
            un=input("Enter Username : ")
            pw=input("Enter Password : ")
            rp=random.randint(1000, 9999)
            cur.execute("select password from ATM_user where username like '%s'" %un)
            while(True):
                e=cur.fetchone()
                if(e==None):
                    break
                else:
                    pas=e[0]
            if(pas==pw):
                print("-"*40)
                print("worning : Record Already Exists...Please Try with different Password")
            else:
                cur.execute("insert into ATM_user values(0, '%s', '%s', %d)" %(un,pw,rp))
                con.commit()
                if(cur.rowcount>0):
                    print("*"*70)
                    print("\tCongratulations....New Account Created Successfully")
                    playsound("C:\\Users\\USER\\Documents\\_Python_\\Project's\\ATM with Database\\sound1.wav")
                else:
                    print("-"*50)
                    print("worning : Record Already Exitsts")
        except:
            cur.execute("insert into ATM_user values(0, '%s', '%s', %d)" %(un,pw,rp))
            con.commit()
            if(cur.rowcount>0):
                print("*"*70)
                print("\tCongratulations....New Account Created Successfully")
                playsound("C:\\Users\\USER\\Documents\\_Python_\\Project's\\ATM with Database\\sound1.wav")
            else:
                print("-"*50)
                print("worning : Record Already Exitsts")

    # Delete Account
    def DelAcc():
        try:
            print("*"*50)
            print("\tDelete Account")
            print("*"*50)
            un=input("Enter username : ")
            pw=input("Enter password : ")
            f=0
            while(True):
                cur.execute("select username,password from ATM_user where username='%s'" %un)
                e=cur.fetchone()
                if(e==None):
                    if(f==0):
                        print("-"*50)
                        print("worning : Record Not Found")
                        break
                    else:
                        break
                else:
                    username=e[0]
                    password=e[1]
                    f=1
                    if(username==un and password==pw):
                        q="delete from ATM_user where username='%s' and password='%s'"
                        cur.execute(q %(un,pw))
                        con.commit()
                        print("*"*50)
                        print("\tAccount Deleted Successfully")
                        playsound("C:\\Users\\USER\\Documents\\_Python_\\Project's\\ATM with Database\\sound2.wav")
                    else:
                        print("-"*50)
                        print("worning : Username and Password Does Not Match")
                        break
        except cx_Oracle.DatabaseError as db:
            print("worning : ",db)
except cx_Oracle.DatabaseError as db:
    print("worning : ",db)
