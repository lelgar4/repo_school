'''
    Richard Elgar
    SDEV220
    Use the Stack class
    
Write a program that displays the first 50 prime numbers in descending order. Use a stack to store prime numbers.        
'''

from Stack import Stack

#   returns true if int passed is prime ; returns false if not; 
#       -- uses modulus operator to determine if 'number' is divisible by any integer other than 1 and itself
def isPrime(number):
    try:
#   if value passed to func is not an instance of integer, raise exception and return false
        if isinstance(number,int) is False:
            raise Exception("Non-integer value passed to function 'isPrime()' ... Value passed: ",number)
        
#   1 is NOT a prime number, even though it technically is only divisible by '1' and itself
        if number > 1:
            
#   for loop, range is 2 - number; prime numbers are ONLY divisible by 1 and themselves; 
#       --  if:     number % !(1 or itself) == 0        >> return false
            for i in range(2,number):
                if number % i == 0:
                    return False
                
            else:   
                return True
            
    except Exception as err:
        print("\n=================================\n\tERROR:\n=================================\n",
              err,"\n\n=================================\n")
        return False


#   program main() 
#       -- creates a Stack object
#       -- finds prime numbers in range 1-250 using func isPrime() then stores them in Stack instance
#       -- after 50 prime numbers are added to stack, creates and displays formatted output; outputs 50 primes in descending order using Stack.pop()
def main():
    primeNums = Stack()         #   instantiate Stack object
    
#   find first 50 prime numbers using for loop with range
    for x in range(1,250):
        
#   if isPrime(x) returns true, add x to top of stack
        if isPrime(x) == True:
            primeNums.push(x)
            
#   check number of prime nums in stack; break loop at 50 and print notification to console
        if primeNums.getSize() >= 50:
            print("\n\n----------------------------------------\n# of prime nums in stack: ",primeNums.getSize(),"\n----------------------------------------\n")
            break
    
#   format output before displaying. use while loop + var formatCtr to display 10 prime nums per console line
    formatCtr = 0
    print("Prime Numbers: ",sep=' ',end=' ')
    while primeNums.isEmpty() == False:         #   while loop iterates until Stack is empty
        
#   after 10 prime nums are printed, reset formatCtr var to 0, move to next line in console
        if formatCtr >= 10:
            formatCtr = 0
            print("\n\t\t",sep='',end='')
             
#   Stack.pop() prime num from Stack >> returns prime num at top of stack and removes it from the Stack
        prime = primeNums.pop()
        
#   formatting if-elif struc; evenly spaces prime nums despite number of digits in prime number;
#       -- 3-digit num >> separate w. 1 space; 2-digit >> 2 spaces; 1-digit >> 3 spaces
        if prime >= 100:
            print(prime,sep=' ',end=' ')
        
        elif prime < 100 and prime >= 10:
            print(prime,sep='  ',end='  ')
            
        elif prime < 10:
            print(prime,end='   ',sep='   ')
            
        formatCtr += 1                          #   incremenet formatCtr
    
    print("\n\n")
        



#   -----------------------------------------------
#       early versions of isPrime(); not used
#   -----------------------------------------------

def isPrimeOne(number):
    for y in range(2,number):
        if number % y == 0:
            return False
    
    return True


def isPrimeTwo():
    for number in range(1,230):
        if number > 1:
            for i in range(2,number):
                if number % i == 0:
                    break
            
            else:   
                print(number,end=' ',sep=' ')
    
    
#   call main()
main()
                    