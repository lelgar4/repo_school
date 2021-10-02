'''
    Richard Elgar
    SDEV220
    Count Single Digits
    Due:

Write a program that generates 1,000 random integers between 0 and 9 and displays the count for each number. 
    Hint: Use a list of ten integers, say counts, to store the counts for the number of 0s, 1s, ..., 9s.)
'''

import random

def main():
#   create empty list; holds counts for ints generated in corresponding list index
    counts = []                         

#   for loop sets values for indicies 0-9 to 0
    for x in range(0,10):               
        counts.append(0)    
            
#   generate 1000 random ints 0-9, increment corresponding counter val in counts[]   
    for i in range(0,1000):
        randNum = random.randint(0,9)
        counts[randNum] += 1        

    print("\n")
#   display count values for each int
    for row in range(0,len(counts)):
        print(row," || ",counts[row])
        print("----------------------------")

#   sum counts and print total 
    sum = 0
    for j in range(0,len(counts)):
        sum = sum + counts[j]
    print("\nTotal: ",sum)

main()