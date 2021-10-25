'''
    Richard Elgar
    SDEV220
    Tkinter: Count the occurrences of each letter

    [14.5] Revise the preceding exercise to display a histogram for the result, as shown in Figure 14.4. You need to display a message in a message box 
    if the file does not exist.

    [14.4] Rewrite Listing 14.5 using a GUI program to let the user enter the file from an entry field, as shown in Figure 14.3a. You can also select a 
    file by clicking the Browse button to display an Open file dialog box, as shown in Figure 14.3b. The file selected is then displayed in the entry 
    field. Clicking the Show Result button displays the result in a text widget. You need to display a message in a message box if the file does not exist.

'''

from tkinter import *
from os.path import isfile
from tkinter.filedialog import askopenfilename
import tkinter.messagebox


class countLetters():
 
    def __init__(self):
        window = Tk()
        window.title("countLetters.py")
        frameCanvas = Frame(window)
        frameCanvas.pack()
        canvas = Canvas(frameCanvas,width=700,height=400)
        canvas.pack()

        frameInput = Frame(window)
        frameInput.pack()
        Label(frameInput,text="Enter file name: ").pack(side=LEFT)
        self.inputFileName = StringVar()
        entryFileName = Entry(frameInput,width=25,textvariable=self.inputFileName).pack(side=LEFT)
        btnBrowse = Button(frameInput,text="Browse",command=self.fileBrowse).pack(side=LEFT)
        btnShowResult = Button(frameInput,text="Show Result",command=self.showResult).pack(side=LEFT)

        window.mainloop()


    def getLetterCounts(self,line,counts):
        for char in line:
            if str(char).isalpha():
                counts[ord(char) - ord('a')] += 1
                

    def fileBrowse(self):
        selectFile = askopenfilename()
        self.inputFileName.set(selectFile)
        self.showResult()


    def showResult(self):
        if isfile(self.inputFileName.get().strip()) == True:
            inputFile = open(self.inputFileName.get().strip())
            listLines = inputFile.readlines()
            counts = 26 * [0]
            
            for line in listLines:
                self.getLetterCounts(line.lower(),counts)
            
            ctCounter = 0
            for ct in counts:
                print(chr(ord('a') + ctCounter), " :: ", str(ct))
                ctCounter+=1
        
        else:
            tkinter.messagebox.showerror("ERROR!","File not found. Try again.")
    



countLetters()