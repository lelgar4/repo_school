'''
    Richard Elgar
    SDEV220
    Game: Nine Heads and Tails
    Due:
Nine coins are placed in a matrix with some face up and some face down. You can represent the state of the coins with the values 0 (heads) and 1 (tails). 

EX:     0 0 0       1 0 1
        0 1 0       0 0 1
        0 0 0       1 0 0

Each state can also be represented using a binary number. For example, the preceding matrices correspond to the numbers:

    000010000       101001100

There are a total of 512 possibilities. So, you can use the decimal numbers 0, 1, 2, 3, ..., and 511 to represent all states of the matrix. 
Write a program that prompts the user to enter a number between 0 and 511 and displays the corresponding 3 * 3 matrix with the characters H and T. 

'''

def main():
#   while loop validates user input. loop is exited when user enters a valid integer, 0 - 511
    while True:

#   get input from user; must be an int 0-511. represents matrix state/possibility
        inpState = input("Enter a number, 0 - 511. The program will then display the corresponding 3 x 3 matrix:\t")

#   check each char in str(input) for letters
        for c in str(inpState):
            if c.isalpha() == True:
                print("ERROR!\nInput can ONLY contain integers.\nTry again.")
                continue

#   check if input is numeric and is between 0 and 511
        if inpState.isnumeric() == True and int(inpState) >=0 and int(inpState) <= 511:
            break
        else:
#   display error message if user input is not 0-511, then repeat input statement
            print("ERROR!\nInput must be an integer 0 to 511, including 0 and 511.\nTry again.")

#   convert input to binary string, e.g. 1 -> '0b1'
    binaryInput = bin(int(inpState))

#   convert binary string to list of chars, slice '0b' from begining of String, e.g. '0b1' -> ['1']
    binaryList = list(binaryInput[2:])

#   convert list elements to integers
    for x in range(0,len(binaryList)):
        if isinstance(binaryList[x],str):
            binaryList[x] = int(binaryList[x])

#   while loop inserts 0's at list[0] index until there are 9 elements -- the number needed to display 3 x 3 matrix
#   e.g. [1] -> [0,0,0,0,0,0,0,0,1]
    while len(binaryList) < 9:
        binaryList.insert(0,0)

#   initialize 2d list for matrix
    matrixList = [[],[],[]]

#   index counter var
    i = 0
#   nested for loops. outer loop = rows in matrix; inner loop = columns.
    for row in range(0,3):
        for col in range(0,3):
#   if element at this index is 0, change to 'H' for heads
            if binaryList[i] == 0:
                matrixList[row].insert(col,'H')
#   if element at this index is 1, change to 'T' for tails
            elif binaryList[i] == 1:
                matrixList[row].insert(col,'T')
            else:
                print("ERROR")
            i += 1
    print("\nInput: ",inpState,"\nBinary: ",binaryInput,"\nMatrix:")
    print("\t",matrixList[0],"\n\t",matrixList[1],"\n\t",matrixList[2],"\n")


#   call main()
main()

