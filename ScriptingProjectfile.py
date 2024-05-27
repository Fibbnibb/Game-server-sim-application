# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:30:13 2024

@author: emeka
"""

#Student Name: David Chukwuemeka Enwesi
#Student Number: A00284023

from abc import ABC, abstractmethod
import time
from datetime import datetime
#now = datetime.now()

#now_dt = now.strftime("%d/%m/%Y %H:%M:%S")

class Account(ABC):
    
    @abstractmethod 
    def __init__(self, name):
        pass
    
    @abstractmethod 
    def provide_info(self):
        pass
              
    @abstractmethod 
    def Login(self):
        pass
    
    @abstractmethod 
    def Logout(self):
        pass
    
class ServerDev(ABC):
    @abstractmethod 
    def __init__(self, name):
        #white list 
        #black_list
        #server_status
        pass
              
    @abstractmethod 
    def Turn_on(self):
        pass
    
    @abstractmethod 
    def Turn_off(self):
        pass
    

###############################################################################    Admin

class Admin(Account):
    def __init__(self, priveledge , name):
        self.name = name
        self.priveledge = 15
        self.priv = str(self.priveledge)
        self.status = "Logged Out"
        
    def provide_info(self):
        print("Priority Level: " + str(self.priveledge) + " Status: " + self.status)
        
    def show_palyer_list(self):
        if Admin.status == "Logged In":
            print(self.account_list)
        else:
            print("[Log in to show list]")
            
    def show_server_log(self):
        print("Opening msg........")
        time.sleep(3)
        with open(Server.message_logfile, "a") as file2:
            now = datetime.now()
            now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
            file2.write('\n'+now_dt +'\t'+ self.name+'\t'+"LOG-REQ"+'\t'+self.priv)
        Server.display_msgs()
        
    def show_server_msg(self):
        print("Opening msg........")
        time.sleep(3)
        with open(Server.message_logfile, "a") as file5:
            now = datetime.now()
            now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
            file5.write('\n'+now_dt +'\t'+ self.name+'\t'+"MSG-REQ"+'\t'+self.priv)
        Server.display_logs()
        
    def Login(self,server):
        self.status = "Logged In"
        Server.add_account(self , self.name)
        with open(Server.message_logfile, "a") as file2:
            now = datetime.now()
            now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
            file2.write('\n'+now_dt +'\t'+ self.name+'\t'+"LOGIN"+'\t'+ self.priv)
        print("....Logged In")
        
    def Logout(self,server):
        self.status = "Logged Out"
        Server.remove_account(self, self.name)
        with open(Server.message_logfile, "a") as filee:
            now = datetime.now()
            now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
            filee.write('\n'+now_dt +'\t'+ self.name+'\t'+"LOGOUT"+'\t' + self.priv)
        print("Logged Out")
        
    def Ban(self):
        if self.status == "Logged In":
            Server.show_account_list(self)
            player_name = input("Enter the player you want to ban: ")
            if player_name in AccountManager.account_dict:
                player = AccountManager.account_dict[player_name]
                Server.remove_account(self, player)
                Server.banned_list.append(player_name)
                player.Logout(self)
                player.status = "Banned"
                with open(Server.message_logfile, "a") as file2:
                    file2.write('\n'+player_name + " was Banned "+"|")
                with open(Server.message_file, "a") as file3:
                    now = datetime.now()
                    now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
                    file3.write('\n'+now_dt +'\t'+ self.name+'\t'+"BAN"+'\t' + 
                                self.priv + '\t\t' +str(player))
                print("Player was Banned")
            else:
                print("[Invalid Player not there]")
        else:
            print("[Log in to Ban]")

    def Unban(self):
        if self.status == "Logged In":
            Server.show_banned(self)
            print
            player_name = input("Enter the player you want to unban: ")
            if player_name in AccountManager.account_dict:
                player = AccountManager.account_dict[player_name]
                Server.restore_acc(self, player)
                player.status = "Unbanned"
                player.Logout(self)
                print(player_name + " is Unbanned")
                with open(Server.message_logfile, "a") as file7:
                    file7.write('\n'+player_name + " was Unbanned "+"|")
                with open(Server.message_file, "a") as file3:
                    now = datetime.now()
                    now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
                    file3.write('\n'+now_dt +'\t'+ self.name+'\t'+"UNBAN"+'\t' + 
                                self.priv+ '\t\t' +str(player))
            else:
                print("[Invalid Player not there]")
        
###############################################################################   Moderator
class Moderator(Account):
    def __init__(self, priveledge , name):
        self.name = name
        self.priveledge = 2
        self.priv = str(self.priveledge)
        self.status = "Logged Out"
    
    def provide_info(self):
        print("Priority Level: " + str(self.priveledge) + " Status: " + self.status)
        
    def Login(self,server):
        self.status = "Logged In"
        Server.add_account(self , self.name)
        with open(Server.message_logfile, "a") as file2:
            now = datetime.now()
            now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
            file2.write('\n'+now_dt +'\t'+ self.name+'\t'+"LOGIN"+'\t'+ self.priv)
        print("....Logged In")
        
    def Logout(self,server):
        self.status = "Logged Out"
        Server.remove_account(self, self.name)
        with open(Server.message_logfile, "a") as file2:
            now = datetime.now()
            now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
            file2.write('\n'+now_dt +'\t'+ self.name+'\t'+"LOGOUT"+'\t'+ self.priv)
        print("Logged Out")
        
    def display_logs(self):
        print("Opening logs........")
        time.sleep(3)
        print("____________________")
        with open(Server.message_logfile, "a") as file2:
            now = datetime.now()
            now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
            file2.write('\n'+now_dt +" : "+ self.name+'\t'+"LOG-REQ"+'\t'+self.priv)
        Server.display_logs()
        
    def display_msgs(self):
        print("Opening msgs........")
        time.sleep(3)
        print("____________________")
        with open(Server.message_logfile, "a") as file2:
            now = datetime.now()
            now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
            file2.write('\n'+now_dt +'\t'+ self.name+'\t'+"MSG-REQ"+'\t'+self.priv)
        Server.display_msgs()
    
###############################################################################   Player
class Player(Account):
    def __init__(self, priveledge , name):
        self.name = name
        self.priveledge = 1
        self.priv = str(self.priveledge)
        self.status = "Logged Out"
    
    def provide_info(self):
        print("Priority Level: " + str(self.priveledge) + " Status: " + self.status)
    
    def Login(self,server):
        if not self.status == "Banned":
            self.status = "Logged In"
            Server.add_account(self , self.name)
            with open(Server.message_logfile, "a") as file2:
                now = datetime.now()
                now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
                file2.write('\n'+now_dt +'\t'+ self.name+'\t'+"LOGIN"+'\t' + self.priv)
            print("....Logged In")
        else:
            print("[This account is no longer allowed in this server]")
        
    def Logout(self,server):
        if not self.status == "Banned":
            self.status = "Logged Out"
            Server.remove_account(self, self.name)
            with open(Server.message_logfile, "a") as file2:
                now = datetime.now()
                now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
                file2.write('\n'+now_dt +'\t'+ self.name+'\t'+"LOGIN"+'\t' + self.priv)
            print("Logged Out")
        else:
            print("[This account is no longer allowed in this server]")

    def send_message(self):
        if self.status == "Logged In":
            print(Server.account_list)
            recv = input("Enter the reciever: ")
            if recv in Server.account_list:           
                message = input("Message-> ")
                message = str(message)
                with open(Server.message_file, "a") as file:
                    now = datetime.now()
                    now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
            # Write text into the file
                    file.write('\n'+now_dt+'\t'+self.name + "->" + recv +"|: "+ message)
                with open(Server.message_logfile, "a") as filemsg:
                    filemsg.write('\n' + now_dt +'\t'+ self.name+'\t'+ "SEND" +'\t'+ recv)
            else:
                print("[Reciever not found in player list]")
               
        elif self.status == "Banned":
            print("[This acccount has been banned]")
        else: #self.status == "Logged out":
            print("[You need to be logged in to send a message]")

###############################################################################   Guest     
class Guest(Account):
    def __init__(self, priveledge , name):
        self.name = name
        self.priveledge = 0
        self.priv = str(self.priveledge)
        self.status = "Logged Out"
    
    def provide_info(self):
        print("Priority Level: " + str(self.priveledge) + " Status: " + self.status)
        
    def Login(self,server):
        if not self.status == "Banned":
            self.status = "Logged In"
            Server.add_account(self , self.name)
            with open(Server.message_logfile, "a") as file2:
                now = datetime.now()
                now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
                file2.write('\n'+now_dt +"\t"+ self.name+'\t'+"LOGIN"+'\t' + self.priv)
            print("....Logged In") 
        else:
            print("This account is no longer allowed in this server")
        
    def Logout(self,server):
        if not self.status == "Banned":
            self.status = "Logged Out"
            Server.remove_account(self, self.name)
            with open(Server.message_logfile, "a") as file2:
                now = datetime.now()
                now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
                file2.write('\n'+now_dt +"\t"+ self.name+'\t'+"LOGOUT"+'\t'+ self.priv)
            print("Logged Out")
        else:
            print("[This account is no longer allowed in this server]")
################################################################################   Server    
class Server(ServerDev):
    #account_dict = {}
    banned_list = []
    account_list = []
    message_logfile = "logfile.txt"
    message_file = "msg.txt"
    def __init__(self, server_name):
        self.server = server_name
        #self.account_dict = {}
        self.blacklist = []
        self.server_status = "Offline"
        
    def add_account(self, account):
        if account not in Server.account_list:
            #For now not going to use dictionaries
            Server.account_list.append(account)
            print("\n\t[Added Account]")
            
    def remove_account(self, account):
       if account in Server.account_list:
           Server.account_list.remove(account)
           print("\n\t[Deleted Account]")
           
    def restore_acc(self,account):
        if account in Server.banned_list:
            Server.banned_list.remove(account)
            Server.account_list.append(account)
    
    def show_account_list(self):
        print(Server.account_list)
    
    def show_banned(self):
        print(Server.banned_list)
        
    def log_message(self, sender, receiver, message):
        with open(self.message_logfile, "a") as file:
            file.write(f"From: {sender.name} | To: {receiver.name}\n{message}\n\n")
            
    def display_logs():
        with open(Server.message_logfile, "r") as file:
            print(file.read())
    
    def display_msgs():
        with open(Server.message_file, "r") as file:
            print(file.read())
    
    def server_send_message(self, sender_name, receiver_name, message):
        sender = Server.find_account(sender_name)
        receiver = Server.find_account(receiver_name)
        if sender and receiver:
            sender.send_message(receiver, message)
        else:
            print("Sender or receiver not found.")
            
    def find_account(self, name):
        for name in Server.account_list:
            if name.name == name:
                return name
        return None

################################################
#Manages the account
class AccountManager:
    account_dict = {}
    def __init__(self):       
        self.priv_dict = {}
        self.server_list = []
        self.banned_list = []

    def add_account(self, privilege, name):
        account = AccFactory.buildAcc(privilege, name)
        AccountManager.account_dict[name] = account
        self.priv_dict[privilege] = name
        
    def add_server(self,server_name):
        AccFactory.buildServer(server_name)
        self.server_list.append(server_name)
        
    # add a remove function for the ban
        
    def server_options(self , server_name):
        server_name = input("Enter your server name: ")
        if server_name in Server.account_list:
            print("Showing Accounts......")
            print(Server.account_list)

    def manage_account(self, name):
        while True:
            if name in self.account_dict:
                account = self.account_dict[name]
                print("""Functions: \nShow info (sh) \nLogin (li) \nLogout (lo) 
                      \nOther (oth)""")
    
                choice = input("What do you want to do: ")
                
                try:
                    if choice == 'sh':
                        account.provide_info()
                    elif choice == 'li':
                        inp = input("Enter the server you want to connect to: ")
                        if inp not in self.server_list:
                            print(".....Not a SERVER")
                        else:
                            account.Login(inp)
                    elif choice == 'lo':
                        inp = input("Enter the server you want to DISconnect from: ")
                        if inp in self.server_list:
                            account.Logout(inp)
                        # Additional actions based on privilege level
                    elif choice == "oth":
                        if account.priveledge == 15:  # Admin
                            print("(15)")
                            admin_choice = input("""Admin-specific action 
                                                 \nPlayer list (lst), 
                                                 \nBan Player (bn), 
                                                 \nUnban Player (unbn), 
                                                 \nShow Server logs (log): """)
                            if admin_choice == 'bn':
                                account.Ban()
                            elif admin_choice == 'unbn':
                                account.Unban()
                            elif admin_choice == 'lst':
                                Server.show_account_list(self)
                            elif admin_choice == 'log':
                                account.show_server_log()
                            else:
                                print("[Invalid option]")
                        elif account.priveledge == 2:  # Moderator
                            print("(2)")
                            moderator_choice = input("""Moderator-specific action 
                                                     \nView logfile (log), 
                                                     View messagefile """)
                            if moderator_choice == "log":
                                account.display_logs()
                            elif moderator_choice == "msg":
                                account.display_msgs()
                            else:
                                print("[Invalid option]")
                        elif account.priveledge == 1:
                            print("(1)")
                            player_choice = input("""Player-specific action 
                                                  \nSend Message (snd): """)
                            if player_choice == "snd":
                                account.send_message()
                            else:
                                print("[Invalid option]")
                except ValueError:  # Handle ValueError here
                        print("[Not a valid option]")
                        # Perform moderator-specific action
                    # Add more conditions based on privilege levels as needed
                again = input("Do you want to perform another action? (yes/no): ")
                if again.lower() != 'y':
                    break  # Exit the loop if the user does not want to continue managing the account
    
                # else:
                #     print("Not an Option")
            else:
                print("Account not found in the player list")

           

################################################
      
class AccFactory:
    @staticmethod
    def buildAcc(priveledge, name):
        if priveledge == 0:
            return Guest(priveledge , name)
        if priveledge == 1:
            return Player(priveledge , name)
        if priveledge == 2:
            return Moderator(priveledge , name)
        if priveledge == 15:
            return Admin(priveledge , name)
        #ignore the 99 priv
        if priveledge == 99:
            return Server(name)
        else:
            print("invalid priority")
            
    @staticmethod 
    def buildServer(server):
        if server == 1:
            return Server()
        else:
            print("invalid option")

#ignore ServerFac
class ServerFac:
    @staticmethod 
    def buildServer(server):
        if server == 1:
            return Server()
        else:
            print("invalid option")