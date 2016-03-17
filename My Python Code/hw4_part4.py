#File: hw4_part4.py
#Author: Julio Gamarra
#Date: 2/29/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for part 4 of hw4 for my CMSC 201 class.

def main():

    #asks user to input a string
    string = input("Please enter a string: ")
    vowels = 0

    #for loop used to iterate through "string"
    for a in string:
        #conditions for vowel or not
        if (a == "a" or a == "A" or a == "e" or a == "E" or a == "i" or a == "I" or a == "o" or a == "O" or a == "u" or a == "U" or a == "y" or a == "Y"):
            #adds 1 to the vowel counter
            vowels = vowels + 1

    print("There are", vowels, "vowels in the string '" + string + "'")

main()
