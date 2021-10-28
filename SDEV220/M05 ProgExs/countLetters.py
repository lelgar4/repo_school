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

#   GUI constructor
    def __init__(self):
        window = Tk()
        window.title("countLetters.py")

#   frame for canvas for results histogram
        frameCanvas = Frame(window)
        frameCanvas.pack()
        self.histogramCanvas = Canvas(frameCanvas,width=700,height=400)
        self.histogramCanvas.pack()
        self.HISTO_BAR_WIDTH = 25
        self.GRAPH_BASE = 350

#   frame for remaining widgets/controls
        frameInput = Frame(window)
        frameInput.pack()
        Label(frameInput,text="Enter file name: ").pack(side=LEFT)
        self.inputFileName = StringVar()
        entryFileName = Entry(frameInput,width=60,textvariable=self.inputFileName).pack(side=LEFT)
        btnBrowse = Button(frameInput,text="Browse",command=self.browseFiles).pack(side=LEFT)
        btnShowResult = Button(frameInput,text="Show Result",command=self.showResult).pack(side=LEFT)

        window.mainloop()

#   iterates characters in a line read from a file; counts occurrences of each letter, a-z
    def getLetterCounts(self,line):
        try:
#   foreach character in a line, if the character is a letter, increment that letters index in list 'counts'
            for char in line:                   
                if str(char).isalpha():         
                    self.counts[ord(char) - ord('a')] += 1

#   foreach value in list 'counts' if value is less than 0 or not an instance of Integer, then it is invalid; throw exception
            for ct in self.counts:
                if ct < 0 or isinstance(ct,int) == False:
                    raise ValueError("ERROR: INVALID COUNT VALUE!")
        
#   ignore indexOutOfBounds exceptions when iterating lines
        except IndexError:
            pass

#   ValueError/invalidCountValue Exception displays messagebox error message
        except ValueError as invalidCountValue:
            tkinter.messagebox.showerror("ERROR! INVALID COUNT VALUE\nOccurrence values for each letter must be integers, greater than or equal to 0.\nTry again.")
            print("-----------------------------------------------------")
            print(invalidCountValue)
            print("-----------------------------------------------------")
    

#   displays histogram of occurrences of each letter in file
    def displayHistogram(self):
        self.histogramCanvas.delete("tkHistogram")      #   clear canvas of previous histogram
        self.histogramCanvas.create_line(10,self.GRAPH_BASE,600,self.GRAPH_BASE,tag="tkHistogram")      #   create base-line for graph
        histBarX1Counter = 20       #   counter var, tracks X(0) of next histo bar/X(1) of previous histobar

#   for each letter/index of 'counts' list: 
        for i in range(26):
#   add corresponding letter below histobar/histograph baseline
            self.histogramCanvas.create_text(histBarX1Counter+2,self.GRAPH_BASE + 8,text=chr(i+ord('a')), tag="tkHistogram")

#   draws a rectangle for current letter histo bar. 
            self.histogramCanvas.create_rectangle(histBarX1Counter-9,self.GRAPH_BASE - self.counts[i],histBarX1Counter + self.HISTO_BAR_WIDTH -9,self.GRAPH_BASE,tag="tkHistogram")

#   increment histBarX1Counter by HISTO_BAR_WIDTH so next histo bar doesn't overlap
            histBarX1Counter += self.HISTO_BAR_WIDTH

                
#   calls askopenfilename, allows user to browse local directories to find a file instead of typing in the file's absolute path
    def browseFiles(self):
        selectFile = askopenfilename()              #   opens filedialoge / browser box from tkinter; selected file's path is set to 'selectFile'
        self.inputFileName.set(selectFile)          #   set instance var inputFileName to file selected by user
        self.showResult()                   


#   opens target file; counts occurrences of each letter in file, then calls displayHistogram() 
    def showResult(self):
        if isfile(self.inputFileName.get().strip()) == True:                #   verify file name/path
            inputFile = open(self.inputFileName.get().strip())              #   open file
            listLines = inputFile.readlines()                       #   create list 'listLines' each list index == a line from the file
            self.counts = 26 * [0]                                  #   init 'counts' as list with 26 indicies

#   foreach loop calls getLetterCounts() for each line of list 'listLines'
            for line in listLines:
                self.getLetterCounts(line.lower())
            
#   prints "[letter] :: [number of occurrences]" for each letter/index of 'counts' to the console
            ctCounter = 0
            for ct in self.counts:
                print(chr(ord('a') + ctCounter), " :: ", str(ct))
                ctCounter+=1

#   call displayHistogram() func to display histogram in canvas.
            self.displayHistogram()

#   display error messagebox; notifies user that the file they input was not found.
        else:
            tkinter.messagebox.showerror("ERROR!","File not found. Try again.")
    
#   initialize program instance
countLetters()