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
        fileName = input("Enter a filename: ").strip()
        while True:
            if isfile(fileName) == True:
                break
            
            else:
                print("\n-----------------------------------------------------\
                        \nERROR!\nFile not found.\nCheck spelling and ensure the file is in the same directory as replaceText.py\
                        \n-----------------------------------------------------\n")
                fileName = input("Enter a filename: ").strip()

        oldString = str(input("Enter the old string to be replaced: ")).strip()
        newString = str(input("Enter the new string to replace the old string: ")).strip()
        listLines = list()
        readFile = open(fileName,"r+")

        for line in readFile:
            if line.find(oldString) != -1:
                line = line.replace(oldString,newString)

            elif line.find(oldString.lower()) != -1:
                line = line.replace(oldString.lower(),newString.lower())

            elif line.find(oldString.capitalize()) != -1:
                line = line.replace(oldString.capitalize(),newString.capitalize())

            elif line.find(oldString.upper()) != -1:
                line = line.replace(oldString.upper(),newString.upper())

            listLines.append(line)
        
        readFile.close()
        writeFile = open(fileName,"w")
        for line in listLines:
            writeFile.write(line)
        
        writeFile.close()   

    except Exception as err:
        print(err)


#   call main()
main()
