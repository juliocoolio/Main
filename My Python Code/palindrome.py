#File: palindrome.py
#Author: Julio Gamarra
#Date: 2/3/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for lab4 for my CMSC201 class.

def main():
    #asks user to input a string
    string = input("Enter a string: ")
    length = len(string)
    reverseString = ""

    for a in range(length - 1, -1, -1):
        reverseString = reverseString + string[a]
    print("The reverse string is:",  reverseString)
    if (string == reverseString):
        print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome")

main()
