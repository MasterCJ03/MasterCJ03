#This program is created by Calla Jones

import time

def password_checker(name,nameLists):
    if name in nameLists.split():
        print(name + " is a common password." )
        try_again=input("Would you like to check another password?\n")
        if try_again==("yes"):
            Menu()
        else:
            print("Thanks for using the password checker")
    else:
        print( name + " is not a common password.")
        time.sleep(5)
        
def Menu():
    name = input("What is a password you want to see if it is common?\n")
    time.sleep(2)
    print("Please Wait, Checking.")
    time.sleep(2)
    nameLists='rockyou.txt','r'
    password_checker(name, nameLists)
Menu()
