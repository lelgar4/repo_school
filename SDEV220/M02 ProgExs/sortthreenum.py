'''
    Richard Elgar
    SDEV220
    Sort three numbers
    DUE: 14 Sep 21

    Write the following function to display three numnbers in increasing order:
        >>  def displaySortedNumbers(num1,num2,num3):
    
    Write a test program that prompts the user to enter three numbers and invokes the function to display them in increasing order
        -- Also write a function that sorts the numbers in decreasing order.
'''

#   sort in increasing order
def displayIncreasing(num1,num2,num3):
    numMax = max(num1,num2,num3)
    numMin = min(num1,num2,num3)
    if(numMax == num1):
        if(numMin == num2):
            numMid = num3
        elif(numMin == num3):
            numMid = num2
    elif(numMax == num2):
        if(numMin == num1):
            numMid = num3
        elif(numMin == num3):
            numMid = num1
    elif(numMax == num3):
        if(numMin == num1):
            numMid = num2
        elif(numMin == num2):
            numMid = num1
    
    print("Numbers in increasing order: ", numMin,numMid,numMax)


#   sort in decreasing order
def displayDecreasing(num1,num2,num3):
    if(num1 == max(num1,num2,num3)):
        numMax = num1
        numMid = max(num2,num3)
        numMin = min(num2,num3)
    elif(num2 == max(num1,num2,num3)):
        numMax = num2
        numMid = max(num1,num3)
        numMin = min(num1,num3)
    elif(num3 == max(num1,num2,num3)):
        numMax = num3
        numMid = max(num1,num2)
        numMin = min(num1,num2)
    
    print("Numbers in decreasing order: ", numMax,numMid,numMin)


#   main function
def main():
    input1,input2,input3 = eval(input("Enter three numbers separated by commas(e.g. '1,2,3'): "))
    displayIncreasing(input1,input2,input3)
    displayDecreasing(input1,input2,input3)


#   call main() 
main()
