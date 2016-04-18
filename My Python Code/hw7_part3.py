#File: hw7_part3.py
#Author: Julio Gamarra
#Date: 4/4/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for part 3 of hw7 for my CMSC 201 class.

def main():

    #asks user to input a filename
    fileName = input("Please enter the name of the file to open: ")

    #splits the filename by period and assigns it to a new variable
    fileNamePeriod = fileName.split(".")
    #while loop to keep asking user for a filename until its ending is correct
    while (fileNamePeriod[-1] != "txt" and fileNamePeriod[-1] != "dat"):
        print("The file must end in .txt or .dat to be valid.")
        fileName = input("Please enter the name of the file to open: ")
        fileNamePeriod = fileName.split(".")

    myFile = open(fileName, "r")
    readMyFile = myFile.read()
    #splits the content of the file by spaces, puts it into a list, and assigns i\
t to a new variable
    readMyFileSpace = readMyFile.split()
    #assigns to a variable the length of the list created by splitting the conten\
t of the file
    words = len(readMyFileSpace)
    print("The file", fileName, "has", words, "words in it.")

    characters = 0
    #for loop to iterate over the created list of strings
    for a in readMyFileSpace:
        #for loop to iterate over each string of characters within the list
        for p in a:
            characters = characters + 1

    #calculates the average word length
    averageWordLength = characters / words
    print("On average, each word is", averageWordLength, "characters long.")
	
	
    sentences = 0
    #splits the content of the file by period, puts it into a list, and assigns i\
t to a new variable
    readMyFilePeriod = readMyFile.split(".")
    for i in readMyFilePeriod:
        sentences = sentences + 1
    print("There are", sentences, "sentences in the file.")

    myFile.close()

main()
