'''
    Richard Elgar
    SDEV220
    Check password
    due 14 Sep 21

Write a function that checks whether a string is a valid password. Suppose the password rules are as follows:
    -- at least 9 characters
    -- only consists of letters and digits
    -- 3 of the chars are digits  
'''

import sys


def checkPassword(password):
#   boolean vars for testing three parameters for a valid password 
    boolLength = False
    boolAlphaNumeric = False
    boolThreeDigits = False

#   check length of password is greater than or equal to 9
    if(len(password) >= 9):
        boolLength = True
    else:
        print("INVALID PASSWORD\n\nPassword is not long enough -- must be 9 characters or longer.\n\ntry again.")
        sys.exit()

#   check the password is alphanumeric -- only contains letters and numbers
    if(password.isalnum()):
        boolAlphaNumeric = True
    else:
        print("INVALID PASSWORD\n\nPassword must ONLY contain letters and numbers.\n\ntry again.")
        sys.exit()

#   check password contains at least three digits
    numCtr = 0
    for ch in password:
        if(ch.isdigit()):
            numCtr = numCtr + 1
    
    if(numCtr >= 3):
        boolThreeDigits = True
    else:
        print("INVALID PASSWORD\n\nPassword must contain AT LEAST three numbers.\n\ntry again.")
        sys.exit()

    if(boolLength and boolAlphaNumeric and boolThreeDigits):
        print("PASSWORD IS VALID")
    


#   function to test checkPassword()
def test():
    password = input("Enter password to be validated: ")
    checkPassword(password)


#   call test()
test()