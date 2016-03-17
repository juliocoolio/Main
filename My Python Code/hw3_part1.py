#File: hw3_part1.py
#Author: Julio Gamarra
#Date: 2/22/16
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is a program for part 1 of hw3 of my CMSC 201 class.

def main():
    #asks user for a number
    number = float(input("Human, enter a floating point number: " ))
    if number > 0:
        print ("The number", number, "is a positive number.")
    if number < 0:
        print ("The number", number, "is a negative number.")
    if number == 0:
        print ("The number", number, "is equal to 0.")


main()
