'''     Richard Elgar
        SDEV220
        Geometry: area of a hexagon
        DUE: 31 AUG 21

Write a program that prompts the user to enter the side of a hexagon and displays its area. 
The formula for computing the area of a hexagon is: 

    Area = ( 3(sqrt(3)) / 2 ) * s^2     

Where s is the length of a side. Also compute and display the perimeter of the hexagon
'''

import math


# input() to get user input for length of hexagon side
# eval() converts input from String to numerical value
side = eval(input("Enter a numerical value for the length of the sides of the hexagon: "))

# formula from programming ex 
area = ( (3 * math.sqrt(3)) / 2 ) * side**2


# perimeter of a hexagon is the sum of all 6 sides, or side * 6
perimeter = side * 6

# output statements
print("for a hexagon with a side length of ", side)
print("Area: ",format(area,"10.2f"))
print("Perimeter: ", perimeter)

