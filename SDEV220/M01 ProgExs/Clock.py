'''     Richard Elgar
        SDEV220
        Turtle: display a clock
        DUE: 31 AUG 21

Write a program that displays a clock to show the time 6:45:00
'''

import turtle


turtle.pencolor("black")    #set pencolor
turtle.pensize(2)
turtle.penup()
turtle.goto(0,-300)         
turtle.pendown()
turtle.circle(300)          #draw outline of clock


'''                     grid used to align numbers on clock
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.pensize(1)
turtle.goto(0,300)
turtle.goto(0,-300)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(300,0)
turtle.goto(-300,0)
turtle.pensize(2)
'''

# move to top -- center x axis, positive/up on y-axis then write 12
turtle.penup()
turtle.goto(-15,260)
turtle.pendown()
turtle.write(12, font = ("Times",24,"bold"))        

# move to right -- positive/right x-axis, center y-axis then write 3
turtle.penup()
turtle.goto(270,-18)
turtle.pendown()
turtle.write(3, font = ("Times",24,"bold"))

# move to bottom -- center x axis, negative/down on y-axis then write 6
turtle.penup()
turtle.goto(-7,-290)
turtle.pendown()
turtle.write(6, font = ("Times",24,"bold"))

# move to left -- negative/left x axis, center y-axis the write 9
turtle.penup()
turtle.goto(-285,-17)
turtle.pendown()
turtle.write(9, font = ("Times",24,"bold"))

# draw hour hand, pointing to 6
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.pensize(8)
turtle.goto(0,-160)

# draw minute hand, pointing to 9 for 45 after
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.pensize(5)
turtle.goto(-250,0)

# draw seconds hand
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.pensize(2)
turtle.goto(0,260)

turtle.done()           # pause program so user can view output