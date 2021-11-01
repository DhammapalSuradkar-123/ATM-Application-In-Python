# Login Menu
from Lop import deposite, withdrow, BalInc

def Lmenu(pw):
    while(True):
        print("*"*50)
        print("\t1) Deposite")
        print("\t2) Withdrow")
        print("\t3) Balance Inc.")
        print("\t4) Log Out")
        print("*"*50)
        try:
            ch=int(input("Enter Your Choise : "))
            if(ch==1):
                deposite(pw)
            elif(ch==2):
                withdrow(pw)
            elif(ch==3):
                BalInc(pw)
            elif(ch==4):
                print("*"*50)
                print("\tLog-Out Successful")
                break
            else:
                print("-"*40)
                print("worning : Please Enter valid Choise")
        except ValueError:
            print("-"*40)
            print("worning : Do not Enter String data/special sysmbol/alpha-numeric data")
