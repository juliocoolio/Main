#File: hw4_part2.py
#Author: Julio Gamarra
#Date: 2/29/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for part 2 of hw4 for my CMSC 201 class.

def main():

    #asks user to input a sentence
    sentence = input("Please enter a sentence: ")
    #calculates length of sentence
    length = len(sentence)
    print("Original sentence: ")
    #prints original sentence
    print(sentence)
    print("Every third letter: ")
    #creates a list of numbers that start at 0 and increase by 3 up to the length of the sentence
    myList = list(range (0, length, 3))

    #for loop used to iterate through "myList"
    for a in myList:
        #assigns "thirdLetter" to be the letter corresponding to the number in the a'th place of "myList"
        thirdLetter = sentence[a]
        #prints the "thirdLetter" of the current iteration
        print(thirdLetter, end = "")

    #starts a new line
    print(end = "\n")


main()
