'''     Richard Elgar
        SDEV220
        Reverse number
        DUE: 31 AUG 21

Write a program that prompts the user to enter a four-digit integer and displays the number in reverse order
Instead of printing the numbers in reverse order, print them in the following order:

            3,2,4,1,5.  

So if the reverse order is 5,4,3,2,1, the program will print 3,2,4,1,5
'''

# get five digit integer from user via input() -- don't use eval(), keep input as String type
fiveDigitString = input("Enter a five digit INTEGER: ")

# create an array of single-character Strings from the input, in the order provided by the exercise
# a characters index in original variable = order number - 1 ; e.g. the third integer's original 
# index would be 2, and its new index 0
charArr = [fiveDigitString[2],fiveDigitString[1],fiveDigitString[3],fiveDigitString[0],fiveDigitString[4]]

# .join() function iterates charArr, joining the Strings together with an empty space, then assigning the result to var newString
newString = "".join(charArr)

# output statement
print(newString)

