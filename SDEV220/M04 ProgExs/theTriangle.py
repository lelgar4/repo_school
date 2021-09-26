'''
    Richard Elgar
    SDEV220
    The Triangle (test) Class

1. Draw the UML diagrams for the classes Triangle and GeometricObject. 

2. Implement the Triangle class. Write a test program that prompts the user to enter the three sides of the triangle, 
    a color, and 1 or 0 to indicate whether the triangle is filled. 
    --  The program should create a Triangle object with these sides and set the color and filled properties using 
    the input. 
    --  The program should display the triangle’s area, perimeter, color, and True or False to indicate whether the 
    triangle is filled or not.
'''

from Triangle import *

#   main function -- get input from user for triangle side lengths, color, and filled/not-filled; create instance of Triangle class, set attributes to input values
def main():
    print("Input values for...\
        \nThe three sides of a triangle(e.g. 1.0, 2, or 33.3)\
        \nThe color of the triangle(e.g. 'blue'\
        \nAnd then indicate if the triangle is filled with a '1';or not filled with a '0' ")

#   while loop used to validate input from user. program won't proceed/will continue to loop without valid input
    while True:
        try:    #   try block used to throw different exceptions/error messages

            inpS1 = float(input("Enter the length of the first side: "))        #   get input for three side values,
            inpS2 = float(input("Enter the length of the second side: "))       #   convert to float value 
            inpS3 = float(input("Enter the length of the third side: "))        #   using float()

#   checks to see if side values input by the user violates the Triangle Inequality Theorem
            if(inpS1 > inpS2 + inpS3 or inpS2 > inpS1 + inpS3 or inpS3 > inpS2 + inpS1):
                raise TriangleIneqTheorException        # raise custom exception

#   get input for color and filled/not-filled
            inpColor = input("Enter the color of the triangle: ")
            inpFilled = int(input("Enter a '1' if the triangle is filled, or a '0' if it is NOT: "))

#   validates input for inpFilled; must be 0 or 1
            if(inpFilled != 1 and inpFilled != 0):
                print("ERROR: input for filled/not filled MUST be either '1' (for True) or '0' (for False)..")
                raise ValueError

#   exception block for invalid value input by user
        except ValueError:
            print("Invalid input. Try again.")

#   exception block for custom Triangle Inequality Theorem exception from Triangle class
        except TriangleIneqTheorException:
            print("The Triangle Inequality Theorem states that the sum of any two sides of a triangle must be greater than the third side.\
                \n For example, a triangle with sides of 1, 2 and 3 is invalid.\nTry again.")

#   if no exception is raised, break the while loop and continue main()
        else:
            break

    triangle = Triangle()               #   create instance of Triangle class using constructor method

    triangle.setSide1(inpS1)            #
    triangle.setSide2(inpS2)            #   set Triangle side values from user input
    triangle.setSide3(inpS3)            #
    triangle.setColor(inpColor)         #   set Triangle color
    triangle.setFilled(inpFilled)       #   set Triangle to filled/not-filled

    print(triangle.__str__())           #   call overriden __str__(), outputs a description of the triangles attributes
    

#   call main()
main()