'''
    Richard Elgar
    SDEV220
    Game: ATM Machine

Use the Account class created in Exercise 7.3 to simulate an ATM machine. Create ten accounts in a list with the 
ids 0, 1, ..., 9, and an initial balance of $500.00. 
    --  The system prompts the user to enter an id. If the id is entered incorrectly, ask the user to enter a correct id. 
    Once an id is accepted, the main menu is displayed as shown in the sample run. 

You can enter a choice of:
    --  1 for viewing the current balance 
    --  2 for withdrawing money
    --  3 for depositing money
    --  4 for exiting the main menu 
    
    --  Once you exit, the system will prompt for an id again. So, once the system starts, it won’t stop.
'''

from typing import List
from account import *
import time


#   initializes and returns a list of account instances
def initializeAccts():
    listAccounts = list()

#   creates 10 account instances; w. ID vals: 0, 1, 2, ... to 9
    for i in range(0,10):
        account = Account()                
        account.setId(i)
        account.setBalance(500.00)
        listAccounts.append(account)            #  new account instance appended to listAccounts
        
    return listAccounts


#   user enters account id to log in
def login(listAccounts):
    print("\n---------------------------\nWelcome To PyBank\n---------------------------")
    inputID = int(input("Enter Your Account ID to Login: "))

#   while loop for validating input for account ID. 
    while True:
        for acct in listAccounts:           #   inner foreach loop -- iterates account instances in listAccounts and compares 
            if(acct.getId() == inputID):    #   their id values to inputID. if the id's match, the login is succesful and that account 
                return acct                 #   instance is returned by login()
        
        print("\nERROR\nInvalid Account ID Entered -- Please try again.\n")
        print("\n---------------------------\nWelcome To PyBank\n---------------------------")
        inputID = int(input("Enter Your Account ID to Login: "))


#   returns text formatted as the ATM's main menu
def dispMainMenu():
    print("\n------------------------------------\n\t\tMain Menu\n------------------------------------")
    print("Please select one of the following: \n[1] -- Check account balance\n[2] -- Make a withdraw\
        \n[3] -- Make a deposit\n[4] -- Log out")


#
def main():
#   initialize list of accounts, then call login function for user auth
    listAccounts = initializeAccts()        
    userAcct = login(listAccounts)

#   while loop loops user interaction w. main menu / menu options. Loop is exited when user selects 'log out' menu option
    while True:
        try:
            dispMainMenu()
            inpMenuOption = int(input("Enter a Menu Option: "))

            if(inpMenuOption != 1 and inpMenuOption != 2 and inpMenuOption != 3 and inpMenuOption != 4):
                raise invalidMenuInputException
            

#   Check Balance / Menu Option 1
            elif inpMenuOption == 1:
                print("\n------------------------------------\nYour Account Balance is: ", \
                    '$' + "{:.2f}".format(userAcct.getBalance()),\
                    "\n------------------------------------\n")
                time.sleep(2.5)
                continue


#   Withdraw / Menu Option 2
            elif inpMenuOption == 2:
                while True:
                    try:
                        inpWithdraw = int(input("Enter Amount to Withdraw -- Must be an Increment of 20: "))
                        if inpWithdraw % 20 != 0:
                            raise wdIncrementException

                        elif inpWithdraw > userAcct.getBalance():
                            raise InsufficientFundsException

                        else:
                            userAcct.withdraw(inpWithdraw)
                            print("\n------------------------------------\nSuccesfully Withdrew ","${:.2f}".format(inpWithdraw),\
                                "\nYour current balance is: ","${:.2f}".format(userAcct.getBalance()),"\n------------------------------------\n\n")
                            time.sleep(2.5)
                            break
#       exception thrown if withdraw input is not an increment of 20
                    except wdIncrementException:
                        print("\nERROR\nWithdraw Amount MUST be an Increment of $20. Try again.\n")
                        continue

#       exception thrown if withdraw amount exceeds account balance
                    except InsufficientFundsException:
                        print("\nERROR\nInsufficient Funds. Try again.\n")
                        continue
                    
                    except ValueError:
                        print("\nERROR\nInvalid Input for Withdraw Amount. Try again.\n")
                        continue
                    except:
                        print("Unexpected Exception @ Menu >> Withdraw >> try:")


#   Deposit / Menu Option 3
            elif inpMenuOption == 3:
                while True:
                    try: 
                        inpDeposit = float(input("Enter Amount to Deposit: "))
                        if(inpDeposit <= 0):
                            print("\nERROR\nInvalid Deposit Amount. Try again.\n")
                        else:
                            userAcct.deposit(inpDeposit)
                            print("\n------------------------------------\nSuccesfully Deposited ","${:.2f}".format(inpDeposit),\
                                "\nYour current balance is: ","${:.2f}".format(userAcct.getBalance()),"\n------------------------------------\n\n")
                            time.sleep(2.5)
                            break
#       exception thrown if user inputs a deposit value that isn't numeric/is a String/contains non-alphanumeric chars
                    except ValueError:
                        print("\nERROR\nInvalid Input for Deposit Amount. Try again.\n")
                    except:
                        print("Unexpected Exception @ Menu >> Deposit >> Try:")


#   Log Out / Menu Option 4
            elif inpMenuOption == 4:
                print("\n\nThank you for choosing to bank with us!\nLogging Out...\n")
                break

#       exceptions thrown if user enters anything other than 1, 2, 3 or 4 at Main Menu
        except invalidMenuInputException:
            print("\nERROR\nInvalid Selection Entered. Please try again.")
            continue
        except ValueError:
            print("\nERROR\nInvalid Selection Entered. Please try again.")
            continue


#   customized exceptions
class invalidMenuInputException(Exception):
    pass

class logOutException(Exception):
    pass

class InsufficientFundsException(Exception):
    pass

class wdIncrementException(Exception):
    pass


#   call main()
main()



