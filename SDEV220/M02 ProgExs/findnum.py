'''     Richard Elgar  
        SDEV220
        Find numbers divisible by 5 or 6, but not both
        DUE: 14 Sep 21

Write a program that displays, ten numbers per line, all the numbers from 100 to 200 that are divisible by 5 or 6, but
not both. The numbers are separated by exactly one space.
      -- Instead of 5 or 6, find numbers that are divisible by 7, but not 8 between 200 - 400
'''

import math


listInts = []           
list2DInts =[[]]        ##  2D list; a list containing list elements
listTemp = []

#   foreach loop; tests each integer starting at 200 and ending at 400
for i in range(200,401):
    if(i % 7 == 0 and i % 8 != 0):          ##  if int 'i' is evenly divisible by 7 (remainder 0) and NOT 8, add to listInts
        listInts.append(i)

#   foreach element in listInts. listTemp is used as a placeholder to make sets of up to 10 elements, which are stored in the 2d list as a list
for x in listInts:
    listTemp.append(x)      
    if(len(listTemp) == 10 or listInts.index(x) == len(listInts) - 1):
        list2DInts.append(listTemp.copy())
        listTemp.clear()

#   removes an empty row/list at index 0 in 2d list from declaration/definition, if it exists
if(len(list2DInts[0]) == 0):
    list2DInts.pop(0)

#   empty string var. used as a string builder to format the output/print
printFormat = ""
colCtr = 0
for x in listInts:
    printFormat = printFormat + str(x) + " "
    colCtr = colCtr + 1
    if(colCtr == 10):
        printFormat = printFormat + "\n"
        colCtr = 0

print(printFormat)

