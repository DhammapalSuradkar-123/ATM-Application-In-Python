# main program
from ATM_Menu import menu
from ATMOp import login,NewAcc,DelAcc
import sys
from playsound import playsound

while(True):
    menu()
    try:
        ch=int(input("Enter your Choise : "))
        if(ch==1):
            login()
        elif(ch==2):
            NewAcc()
        elif(ch==3):
            DelAcc()
        elif(ch==4):
            print("~"*50)
            print("     << _Thank's for Using This ATM Machine_ >>")
            print("~"*50)
            playsound("C:\\Users\\USER\\Documents\\_Python_\\Project's\\ATM with Database\\sound3.wav")
            sys.exit()
        else:
            print("-"*20)
            print("worning: Please Enter the valid Choise.")
    except ValueError:
        print("-"*20)
        print("worning : Do not used string data/special sysmbol/alpha-numeric data")
