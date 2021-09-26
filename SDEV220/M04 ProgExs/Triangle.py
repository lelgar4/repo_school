'''
    Richard Elgar
    SDEV220
    Triangle class

Design a class named Triangle that extends the GeometricObject class. The Triangle class contains:
    --  Three float data fields named side1, side2, and side3 to denote the three sides of the triangle
    --  A constructor that creates a triangle with the specified side1, side2, and side3 with default values 2.0
    --  Accessor methods for all three data fields
    --  A method getArea() that returns the area of the triangle
    --  A method getPerimeter() that returns the perimeter
    --  A method __str__() that returns a string desc for the triangle
'''

import math
from GeometricObject import GeometricObject
from math import *

class Triangle(GeometricObject):        #   class definition extends superclass GeometricObject
#   no arg constructor
    def __init__(self):
        super().__init__()              #   superclass initializer   

        self.__side1 = 2.0              #
        self.__side2 = 2.0              #   set default vals for three sides
        self.__side3 = 2.0              #


#   accessor and mutator methods for three side vars
    def getSide1(self):
        return self.__side1

    def setSide1(self, side):
        self.__side1 = side
    
    def getSide2(self):
        return self.__side2

    def setSide2(self, side):
        self.__side2 = side

    def getSide3(self):
        return self.__side3

    def setSide3(self, side):
        self.__side3 = side


#   returns the area of a triangle using Heron's formula:
#       Area = sqrt(p(p-a)(p-b)(p-c))   
#   where 'p' is half the triangle's perimeter, and a/b/c represent the triangle's 3 sides
    def getArea(self):
        p = self.getPerimeter() / 2
        x = float(p * (p - self.__side1) * (p - self.__side2) * (p - self.__side3)   )
        area = math.sqrt(x)
        return round(area,2)
    
#   returns the perimeter of the triangle -- sum of all three sides
    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3
    
#   overrides superclass method __str__()
#   returns a description of the triangle/triangle's attributes
    def __str__(self):
        return "Color: " + self.getColor() + "\nFilled?: " + str(self.isFilled()) + "\nSide1: " + str(self.getSide1()) + "\nSide2: " + str(self.getSide2()) + "\nSide3: " + str(self.getSide3()) + "\nPerimeter: " + str(self.getPerimeter()) + "\nArea: " + str(self.getArea())

#   overrides superclass method setFilled()
    def setFilled(self, filled):
        if filled == 0:             #   if filled arg is 0, set filled attribute to False
            return super().setFilled(False)
        elif filled == 1:           #   if filled arg is 1, set filled attribute to True
            return super().setFilled(True)

#   custom exception for Triangle Inequality Theorem -- the sum of any two sides of a triangle must be greater than the length of the third side
#   this exception is used to prevent input that would result in an invalid/incorrect area value due to this theorem.
class TriangleIneqTheorException(Exception):
    pass
