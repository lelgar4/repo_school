'''     
        Richard Elgar
        SDEV 220
        Hangman Final Project v2
        15 Dec 21s
'''

import random
from tkinter import *
from tkinter import messagebox


class Hangman:
    def __init__(self):
#   init data field vars
        self.count = 0
        self.missed = ""
        
#   open text file containing list of words; create list and call readlines() to add words from text file to list
        self.file = open("hangman_words.txt", "r")
        self.choices = self.file.readlines()
        
#   instantiate GUI window using tk constructor; set title; initialize canvas and set dimensions
        self.window = Tk()
        self.window.title("Hangman")
        self.canvas = Canvas(self.window, width = 400, height = 300, background = "white")
        self.canvas.pack()
        
#   bind keys to functions
        self.window.bind("<Key>", self.keypress)
        self.window.bind("<Return>", self.newgame)
        
#   randomly select a word from list of words; strip whitespace from word
        self.word = random.choice(self.choices)
        self.word = self.word.strip()
        
#   init fields for GUI; wordGuess == '*'s which are replaced with correctly guessed letters
        self.wordGuess = "*" * (len(self.word))
        self.msg1 = "Guess a Letter: " + self.wordGuess
        self.msg2 = "Missing letters: " + self.missed
        
#   call house constructor; loop window
        self.house()
        self.window.mainloop()


#   clear canvas of elements tagged as 'house'
    def clear(self):
        self.canvas.delete("house")


#   clears canvas then draws house; number of house parts drawn correlates to number of missed guesses
    def house(self):
        self.clear()
        
#   nested if statements; program only reaches if blocks corresponding to number of missed guesses
        if self.count >= 1:
            self.canvas.create_line(75, 200, 75, 100, tags="house")
            
            if self.count >= 2:
                self.canvas.create_line(275, 200, 275, 100, tags="house")
                
                if self.count >= 3:
                    self.canvas.create_line(75, 100, 275, 100, tags="house")
                    
                    if self.count >= 4:
                        self.canvas.create_line(75, 100, 150, 75, tags="house")
                        
                        if self.count >= 5:
                            self.canvas.create_line(275, 100, 150, 75, tags="house")
                            
                            if self.count >= 6:
                                # adding the door to the house
                                self.canvas.create_line(125, 200, 125, 150, tags="house")  # line going up
                                self.canvas.create_line(125, 150, 160, 150, tags="house")  # line going right
                                self.canvas.create_line(160, 150, 160, 200, tags="house")  # line going down
                                
                                if self.count >= 7:
                                    # adding the circular window
                                    self.canvas.create_oval(220, 150, 250, 175, tags="house")

        self.canvas.create_text(200, 250, text=self.msg1, tags="house", font=(12))
        self.canvas.create_text(200, 270, text=self.msg2, tags="house", font=(12))
        return


#   used to block input in specific situations. keypress input is bound to this function to prevent input
    def donothing(self,event):
        return


#   called on key press/user input. function takes key pressed and determines whether or not its corresponding letter
#   is contained in word
    def keypress(self,event):
        key = event.char
        
#   uppercase letters input are turned lowercase
        if key.isalpha():
            if key.isupper():
                key = key.lower()
        
#   return if key/char input is not a letter
        if not key.isalpha():
            return

#   return if key/char input has already been guessed
        elif key in self.missed:
            return
        
#   find if key/char pressed is in word
        else:
            if key in self.word:
                self.missed += key
                
#   foreach iterates each char in word
                for x in range(len(self.word)):
                    
#   if key char matches word char: create new list instance set to current wordGuess
                    if key == self.word[x]:
                        wordList = list(self.wordGuess)
                        
#   set corresponding '*' in word/wordGuess to correctly guessed char, then set wordGuess to updated string
                        wordList[x] = key
                        self.wordGuess = "".join(wordList)
                        
#   udpate fields on GUI, call house constructor
                        self.msg1 = "Guess a Letter: " + self.wordGuess
                        self.msg2 = "Missing letters: "+ self.missed
                        self.house()
                        
#   if user has guessed all chars in word: bind keypresses to doNothing to prevent further input;
#       notify user they have won; call house constructor
                        if self.wordGuess == self.word:
                            self.window.bind("<Key>", self.donothing)
                            self.msg2 = "Congratulations, you win!!!"
                            self.house()
                            
#   if key/char is not in word: add to list of guesses; increment number of missed guesses; call house constructor
#       to update GUI
            else:
                self.missed += key
                self.count += 1
                self.msg1 = "Guess a Letter: " + self.wordGuess
                self.msg2 = "Missing letters: " + self.missed
                self.house()
                
#   if user has 7+ missed guesses they lose; bind keypress to doNothing() to prevent input; notify user they lost;
#       call house constructor to update GUI
        if self.count >= 7:
            self.window.bind("<Key>", self.donothing)
            self.msg2 = "You Lose: Press Enter to play again"
            self.house()

#   inits new game, clears fields
    def newgame(self,event):
        self.window.bind("<Key>", self.keypress)
        self.clear()

#   clear missed letters, reset count to 0
        self.missed = ""
        self.count = 0
        
#   get new word from list
        self.word = random.choice(self.choices)
        self.word = self.word.strip()
        
#   reset remaining fields
        self.wordGuess = "*" * (len(self.word))
        self.msg1 = "Guess a Letter: "+ self.wordGuess
        self.msg2 = "Missing letters: " + self.missed
        self.msg2 = ""
        
#   instantiate house
        self.house()


Hangman()
