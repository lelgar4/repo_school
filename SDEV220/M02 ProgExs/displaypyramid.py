'''     Richard Elgar
        SDEV220
        Display a pyramid
        Due 14 SEP 21

Write a program that prompts the user to enter an integer from 1 to 15 and displays a pyramid
        -- Using the same input number, also dissplay an  inverted triangle. 
'''

lines = int(input("Enter a number of lines: "))
spacing = lines * 2
for x in range(1,lines + 1):
        s = lines + spacing        
        sp = str(s) + "s"
        print(format(" ",str(lines + spacing) + "s"),end='')
        for y in range(x,0,-1):
                print(y,end='')
        for y in range(2,x + 1):
                print(y,end='')

        print(format(" ",sp))
        spacing -= 3



'''
inputInt = eval(input("Enter an integer, 1 to 15"))
if(inputInt <= 15):
        for i in range(1,inputInt + 1):
                if(i != 1):
                        middleNum = math.ceil(inputInt / 2)
                else:
                        middleNum = inputInt

else:
        print("ERROR:\n Input must be an integer, 1 to 15.\n Try again.")
'''