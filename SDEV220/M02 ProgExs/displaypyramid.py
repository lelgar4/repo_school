'''     Richard Elgar
        SDEV220
        Display a pyramid
        Due 14 SEP 21

Write a program that prompts the user to enter an integer from 1 to 15 and displays a pyramid
        -- Using the same input number, also dissplay an  inverted triangle. 
'''

import math


#       returns the base / longest row (for rightside up pyramid). 
#       first list returned = every digit left of the center '1'; second list contains middle '1' -> end going right
def row(input):
        return list(reversed(range(2, input + 1))) + list(range(1, input + 1))


#       prints rightside up pyramid. uses foreach incrementing from 1 to input to print rows starting with '1' -> '2 1 2' -> ...
def printPyramid(rows):
        for i in range(1,rows + 1):
                arrRow = row(i)
                strRow = ""
                for n in arrRow:
                        strRow = str(strRow + str(n)  + " ")
                print(strRow.center(rows * 4))                  #  format/centers rows by adding to a new string w/ 4x as many chars as input


#       prints upside down pyramid. reversed foreach from printPyramid()
def printUpsideDown(rows):
        for i in range(rows,0,-1):
                arrRow = row(i)
                strRow = ""
                for n in arrRow:
                        strRow = str(strRow + str(n)  + " ")
                print(strRow.center(rows * 4))   
        

#       main function. gets input from user for number of rows. then calls functions and 
def main():
        inputRows = int(input("Enter the number of lines/rows to print: "))
        print("Pyramid: \n\n")
        printPyramid(inputRows)

        print("\n\n Upside down pyramid: \n\n")
        printUpsideDown(inputRows)


#       call main()
main()