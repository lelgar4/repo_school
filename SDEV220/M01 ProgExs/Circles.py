'''     Richard Elgar
        SDEV220
        Turtle:  draw  four  circles
        DUE: 31 AUG 21

Write  a  program  that  prompts  the  user  to  enter  the radius of a circle and draws 
SIX circles in the center of the screen
'''

import turtle


# get user input for circle radius
radius = eval(input("Enter the radius of the circles to be drawn: "))


turtle.pencolor("black")           # set turtle pen color
turtle.penup()                  # pickup pen prior to moving pen for first circle
 
# first circle -- negative/left on x-axis, center on y-axis
turtle.goto((1 - radius),0)
turtle.pendown()
turtle.circle(radius)
turtle.penup()

# second circle -- positive/right on x-axis, center on y-axis
turtle.goto(radius,0)
turtle.pendown()
turtle.circle(radius)
turtle.penup()

# third circle -- negative/left on x-axis, positive/up on y-axis
turtle.goto((1 - radius),radius * 2)
turtle.pendown()
turtle.circle(radius)
turtle.penup()

# fourth circle -- positive/right on x-axis, positive/up on y-axis
turtle.goto(radius,radius * 2)
turtle.pendown()
turtle.circle(radius)
turtle.penup()

# fifth circle -- negative/left on x-axis, negative/down on y-axis
turtle.goto((1 - radius),radius * -2)
turtle.pendown()
turtle.circle(radius)
turtle.penup()

# final circle -- positive/right on x-axis, negative/down on y-axis
turtle.goto(radius,radius * -2)
turtle.pendown()
turtle.circle(radius)
turtle.penup()

turtle.done()       # pause program to allow user to view output