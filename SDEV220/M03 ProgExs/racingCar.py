'''
    Richard Elgar
    SDEV220
    Racing Car
    Due: 28 Sep 21

Write a program that simulates car racing, as shown in Figure 9.29b–d. The car moves from left to right. When it reaches the right end, 
it restarts from the left and continues the same process. Let the user increase and decrease the car’s speed by pressing the Up and Down 
arrow keys.
'''

from tkinter import *

class racingCar:

    def moveCar(self):
        self.canvas.move("car",self.dx,0)
        self.canvas.move("frontwheel",self.dx,0)
        self.canvas.move("backwheel",self.dx,0)
        self.canvas.update()

#   track cars x coord; when rear of car reaches edge of window, delete the car and re-create it at x=0
        if(self.x<250):
            self.x += self.dx
        else:
            self.x = 0
            self.canvas.delete("car")
            self.canvas.delete("frontwheel")
            self.canvas.delete("backwheel")
            self.canvas.create_polygon(
                0,(100-10),
                0,(100-20),
                10,(100-20),
                20,(100-30),
                30,(100-30),
                40,(100-20),
                50,(100-20),
                50,(100-10),
                0,(100-10),
                outline="black",
                fill="gray",
                tags="car"
            )
            self.canvas.create_oval(10,(100-10),20,100,fill="black",tags="backwheel")
            self.canvas.create_oval(30,(100-10),40,100,fill="black",tags="frontwheel")
        self.canvas.after(100,self.moveCar)


    def __init__(self):
        window = Tk()
        window.title = "RacingCar.py"
        self.canvas = Canvas(window,bg="white",width="250",height="100")
        self.canvas.pack()
        self.canvas.bind("<Up>",self.rcSpeedUp)
        self.canvas.bind("<Down>",self.rcSlowDown)
        window.focus_set()

        self.canvas.create_polygon(
            0,(100-10),
            0,(100-20),
            10,(100-20),
            20,(100-30),
            30,(100-30),
            40,(100-20),
            50,(100-20),
            50,(100-10),
            0,(100-10),
            outline="black",
            fill="gray",
            tags="car"
        )
        self.canvas.create_oval(10,(100-10),20,100,fill="black",tags="backwheel")
        self.canvas.create_oval(30,(100-10),40,100,fill="black",tags="frontwheel")

        self.dx = 10
        self.x = 0
        self.canvas.after(100,self.moveCar())
        
        window.mainloop()
        

    def rcSpeedUp(self):
        print("Speed + 5")
        self.dx += 5
    
    def rcSlowDown(self):
        if(self.dx >= 10):
            print("Speed - 5")
            self.dx -= 5
        else:
            print("Can't slow down any more.")


racingCar()        