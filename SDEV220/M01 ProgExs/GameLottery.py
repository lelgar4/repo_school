'''     Richard Elgar
        SDEV220
        Game: Lottery
        DUE: 31 AUG 21

Revise  Listing  4.10,  Lottery.py,  to  generate  a  three-digit  lottery number.  The  program  prompts  the  user  to  enter  a 
three-digit  number  and  determines whether the user wins according to the following rules:
        1. If  the  user  input  matches  the  lottery  number  in  the  exact  order,  the  award  is $15,000.
        2. If all the digits in the user input match all the digits in the lottery number (but not in correct order), the award is $7,500.
        3. If two digits in the user input matches two digits in the lottery number, the award is $2,000

        If the user matches ONE OR NONE of the lottery numbers, they win nothing
'''

import random
import array


# generate random int for lottery number, assign same value to a second pointer to retain 
LOTTERY = random.randint(0,999)
lottery2 = LOTTERY

# user inputs a two digit integer, trying to guess the lottery number
GUESS = eval(input("Enter your lottery pick (three digits): "))
guess2 = int(GUESS)


# if EXACT match, including order, user wins $15,000
if guess2 == lottery2:            
        print("EXACT MATCH -- you win $15,000!")
        

else: 
# use modulus and floor division operators to split original value into three separate digits/vars
# 'lottery % 10' expression gets the one's decimal place value of lottery
        lottoOnes = lottery2 % 10
        lottery2 //= 10                         # remainder / one's place is dropped after floor division of lottery by 10 
        lottoTens = lottery2 % 10           # repeat for 10's and 100's place digits
        lottoHundreds = lottery2 // 10                              

# repeat for guess
        guessOnes = guess2 % 10
        guess2 //= 10
        guessTens = guess2 % 10
        guessHundreds = guess2 // 10


# digits for each set of numbers added to array
        lottoArr = [lottoOnes,lottoTens,lottoHundreds]
        guessArr = [guessOnes,guessTens,guessHundreds]

# use nested for-each loops to count matching digits. var matchCtr tracks number of matches
        matchCtr = 0                    
        for guess in guessArr :                                 # outer loop iterates guessArr
                for digit in lottoArr :                         # inner loop iterates lottoArr
                        if guess == digit :                     # if element from guessArr is equal to element from lottoArr
                                print("MATCH: ", guess)         # prints the digit matched          
                                matchCtr += 1                   # increment matchCtr


        if matchCtr == 3 :
                print("MATCHED ALL DIGITS (but not the order) -- you win $7,500!")
        elif matchCtr == 2 : 
                print("MATCHED TWO DIGITS -- you win $2,000!")
        else : 
                print("Sorry, try again")
