'''
    Richard Elgar
    SDEV220
    Find the number of uppercase letters in a string

    Write a recursive function to RETURN the number of uppercase letters in a string using the following function headers:
        
        def countUppercase(s):
        def countUppercaseHelper(s, high):
'''

#   global/class ctr var for number of uppercase letters
ctrUppercase = 0


#   recursive function. calls helper function
def countUppercase(s):
    return countUppercaseHelper(s,len(s) - 1)


#   recursive helper function. 
def countUppercaseHelper(s,high):

    global ctrUppercase         #   ref global ctrUppercase
    if str(s) == '':            #   if 's' is null/empty string, will return '0'
        return ctrUppercase

#   if first char in 's' is uppercase, increment ctrUppercase and return a recursive call of countUppercaseHelper() w/ first char (s[0]) sliced from of 's'
    if str(s[0]).isupper() == True:
        ctrUppercase += 1
        return countUppercaseHelper(s[1:],high - 1)
#   if first char is not upper, return recursive call of countUppercaseHelper() w/o incrementing ctrUppercase
    else:
        return countUppercaseHelper(s[1:],high - 1)


#   main/test function
def main():
    global ctrUppercase         #   ref global var ctrUppercase

#   prompt user to enter a string; input value set to 's'
    print("Enter a string below to count the number of uppercase letters in the string..")
    s = input("Input string: ")

#   call countUppercase(s) and display output
    print("\n------------------------------------------")
    print("Number of uppercase letters: ",countUppercase(s))
    print("------------------------------------------\n")


#   call main
main()
