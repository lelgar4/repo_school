'''
    Richard Elgar
    SDEV220
    Replace Text
    
    Write a program that replaces text in a file. Your program should prompt the user to enter a filename, an old string, and a new string
        --  Replace the word Happy with Merry.
'''

from os.path import isfile

def main():
    try: 
#   prompt user to input filename
        fileName = input("Enter a filename: ").strip()

#   while loop checks if file input by user exists; loop doesn't break until a valid file name is entered.
        while True:
            if isfile(fileName) == True:
                break

#   error message displayed if input doesn't match any existing file names
            else:
                print("\n-----------------------------------------------------\
                        \nERROR!\nFile not found.\nCheck spelling and ensure the file is in the same directory as replaceText.py\
                        \n-----------------------------------------------------\n")

#   prompt user to enter another file name
                fileName = input("Enter a filename: ").strip()

#   prompt user to input old string/string to replace, AND new string/string to replace old string
        oldString = str(input("Enter the old string to be replaced: ")).strip()
        newString = str(input("Enter the new string to replace the old string: ")).strip()

        listLines = list()                  #   init list 'listLines'
        readFile = open(fileName,"r+")      #   open file entered by user in read mode

#   foreach - searches each line of file for instances of 'oldString'; replaces instances of 'oldString' with 'newString' using line.replace()
        for line in readFile:
            if line.find(oldString) != -1:                  #   default
                line = line.replace(oldString,newString)

            elif line.find(oldString.lower()) != -1:        #   search line for lowercase oldString using oldString.lower();           oldString --> "oldstring"
                line = line.replace(oldString.lower(),newString.lower())   

            elif line.find(oldString.capitalize()) != -1:   #   search line for capitalized oldString using oldString.capitalize();     oldString --> "Oldstring"
                line = line.replace(oldString.capitalize(),newString.capitalize())

            elif line.find(oldString.upper()) != -1:        #   search line for uppercase oldString using oldString.upper();            oldString --> "OLDSTRING"
                line = line.replace(oldString.upper(),newString.upper())

            listLines.append(line)                          #   append line to listLines after replacing instances of oldString w/ newString
        
        readFile.close()                                    #   close file
        writeFile = open(fileName,"w")                      #   reopen file in 'write' mode

#   foreach line in list 'listLines', write line to file
        for line in listLines:
            writeFile.write(line)
        
        writeFile.close()           #   close file

    except Exception as err:
        print(err)


#   call main()
main()
