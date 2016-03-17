#File: hw4_part5.py
#Author: Julio Gamarra
#Date: 2/29/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for part 5 of hw4 for my CMSC 201 class.

def main():

    #creates a range of numbers between 1 and 100 (including)
    numbers = range(1,101)

    #for loop used to iterate through "numbers"
    for a in numbers:
        #conditions for varying print statements
        if (a % 3 == 0 and a % 5 == 0):
            print("In the future, everyone will be world famous for 15 minutes.")
        elif (a % 5 == 0):
            print("Where do you see yourself in five years?")
        elif (a % 3 == 0):
            print("Better three hours too soon than a minute too late.")
        else:
            print(a)

main()
