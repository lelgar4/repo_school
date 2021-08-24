'''     Richard Elgar
        SDEV220
        Area and perimeter of a rectangle
        DUE: 31 Aug 21

(Area and perimeter of a rectangle) 
Write a program that displays the area and perimeter of a 
rectangle (USER INPUT FOR WIDTH AND HEIGHT) using the 
following formula:
                    area = width * height
'''
# input() used to get input from user for width and height variables
# eval() converts input from a String to a numeric value
width = eval(input("Enter a numerical value (e.g. '5' or '12.5') for the WIDTH of the rectangle: "))
height = eval(input("Enter a numerical value (e.g. '5' or '12.5') for the HEIGHT of the rectangle: "))

# formula from exercise. area of rectangle is set to the product of user-entered
# values for width and height
area = width * height

# perimeter of a rectange is equal to heigh*2 + width*2
perimeter = width * 2 + height * 2

# output statements
print("The area of a rectangle with a width of ", width, " and a height of ", height, " is equal to ", area)
print("The perimeter of the same rectangle is equal to ", perimeter)