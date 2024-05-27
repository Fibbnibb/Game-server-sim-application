# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 17:23:09 2024

@author: emeka
"""

#Student Name: David Chukwuemeka Enwesi
#Student Number: A00284023

from ScriptingProjectfile import Account
from ScriptingProjectfile import ServerDev

from ScriptingProjectfile import AccFactory
from ScriptingProjectfile import ServerFac

from ScriptingProjectfile import AccountManager
from datetime import datetime
#now = datetime.now()

#now_dt = now.strftime("%d/%m/%Y %H:%M:%S")

try:
    if __name__ == "__main__":
        account_manager = AccountManager()
        with open("logfile.txt" , "a") as filemsg:
            now = datetime.now()
            now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
            filemsg.write('\n' + now_dt +'\t'+ "SES" +'\t'+ "BEGIN" +"\n" )
    
        while True:
            # Your existing menu and choices can be incorporated into the AccountManager class.
            # For example:
            print ("\n----Welcome to the Game Server application----")
            print ("\tWhat tasks do you need performed?\n")
            print("\tPress 1 for Add an Account")
            print("\tPress 2 for Add a Server")
            print("\tPress 3 for Manage Account")
            print("\tPress 4 to Manage Server\n")
            print("\tPress 99 to quit\n")
            choice = int(input("What task do you want to perform?: "))
            
            if choice == 1:
                privilege = int(input("Enter the account type (0, 1, 2, 15): "))
                name = input("(ADD) Enter your Name: ")
                account_manager.add_account(privilege, name)
            elif choice == 2:
                name = input("(ADD) Enter your server Name: ")
                account_manager.add_server(name)
            elif choice == 3:
                name = input("(LOG) Enter your Account Name: ")
                account_manager.manage_account(name)
            elif choice == 4:
                name = input("(LOG) Enter the Server to manage: ")
                
            elif choice == 99:
                with open("logfile.txt" , "a") as filemsg:
                    now = datetime.now()
                    now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
                    filemsg.write('\n' + now_dt +'\t'+ "SES" +'\t'+ "END" +"\n" )
                break
            else:
                print("Invalid choice")    
except ValueError:
    print("[Not a valid option]")
