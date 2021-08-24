'''     Richard Elgar
        SDEV220
        Geometry: area of a pentagon
        DUE: 31 AUG 21

Write a program that prompts the user to enter the length from the center of a pentagon 
to a vertex and computes the area of the pentagon

formula for computing the area of a pentagon:

        Area = ( (3 * sqrt(3)) / 2 ) * side^2

formula for side of a pentagon:

        Side = 2r * sin(PI/5)

where 'r' is the length from the center of the pentagon to a vertex

Also compute and print out the length of the side of the pentagon.
'''

import math


# get user input for length of 'r' with input() function, eval() converts input from String to numerical value
rLength = eval(input("Enter a numerical value for 'r' -- the length between the center and any one vertex of a pentagon: "))

# formula from  exercise for the length of a pentagon's side, given 'r' 
side = 2 * rLength * (math.sin(math.pi/5))

# formula from  exercise to calculate a pentagon's area, given the length of its sides
area = ( (3 * math.sqrt(3)) / 2 ) * side**2

# output statement -- outputs area and length of side, formatted to 2 decimal places
print("For a pentagon with a length of ", rLength, " between its center and its verticies, the length of its sides would be equal to ") 
print(format(side,"10.2f")) 
print(" and its area equal to ")
print(format(area,"10.2f"))