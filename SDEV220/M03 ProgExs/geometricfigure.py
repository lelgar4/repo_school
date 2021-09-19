'''
    Richard Elgar
    SDEV220
    Select Geometric Figures
    Due: 28 Sep 21

Write a program that draws a diamond or a triangle, use selects a figure from a radio button and specifies whether it is filled by selecting a checkbox
'''

from tkinter import *   #  import all from tkinter

class geometricfigure:
    def __init__(self):
#   create window instance, add title
        window = Tk() 
        window.title("Select Geometric Figures")

#   create frame instance, and pack
        frame = Frame(window)
        frame.pack()

#   associate class var figure as an entry/input var
        self.figure = IntVar()

#   creates radiobuttons for selecting diamond/triangle, and a label for those radiobuttons, defines their attributes, then adds 
#   them to the frame's grid
        lblSelectFig = Label(frame, text="Select a figure to display: ")
        rbDiamond = Radiobutton(frame, text="Diamond", variable=self.figure, value=1)
        rbTriangle = Radiobutton(frame, text="Triangle", variable=self.figure, value=2)
        lblSelectFig.grid(row=1,column=1)
        rbDiamond.grid(row=2,column=1)
        rbTriangle.grid(row=2,column=2)

#   associate chkFilled as entry/input var
        self.chkFilled = IntVar()     

#   creates a checkbutton for selecting filled/not-filled and a label for the checkbutton, defines the elements' attributes, then adds 
#   them to the frame's grid
        lblCBFilled = Label(frame, text="Check the box below to make the figure display filled: ")
        cbFilled = Checkbutton(frame, text="Filled?", variable=self.chkFilled)
        lblCBFilled.grid(row=4,column=1)
        cbFilled.grid(row=5,column=1)

#   creates a submit button which triggers the dispFigure() function when clicked
        btnSubmit = Button(frame,text="SUBMIT",command=self.dispFigure)
        btnSubmit.grid(row=7,column=2)

#   create event loop
        window.mainloop()
    

#   displays a diamond or triangle, either filled or unfilled, depending on user input
    def dispFigure(self):
        if(self.figure.get() == 1 or self.figure.get() == 2):   #  ensures one of the two shape radiobuttons are selected before executing 
                                                                #  the rest of the function
            windCanv = Tk()
            windCanv.title("Figure Display")
            self.canvas = Canvas(windCanv,width=900,height=600)
            self.canvas.pack()

            if self.figure.get() == 1:
#   displays a filled diamond
                if(self.chkFilled.get()):
                    self.canvas.create_polygon(
                        200,0,
                        400,200,
                        200,400,
                        0,200
                )
#   displays an unfilled diamond
                else:  
                    self.canvas.create_polygon(
                        200,0,
                        400,200,
                        200,400,
                        0,200,
                        outline="black",
                        fill="white"
                    )

            elif self.figure.get() == 2:
#   displays a filled triangle
                if(self.chkFilled.get()):
                    self.canvas.create_polygon(
                        200,0,
                        400,400,
                        0,400,
                    )
#   displays an unfilled triangle
                else:
                    self.canvas.create_polygon(
                        200,0,
                        400,400,
                        0,400,
                        outline="black",
                        fill="white"
                    )
            else:
                print("ERROR")
                
        else:
            print("ERROR:\n Must select a figure to display. Try again.")


geometricfigure()