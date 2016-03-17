#File: hw4_part1.py
#Author: Julio Gamarra
#Date: 2/29/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for part1 of hw4 for my CMSC 201 class.

def main():

    #asks user to input base number
    baseNumber = int(input("Enter the base number: "))
    #asks user to input max number
    maxNumber = int(input("Enter the max number: "))
    #creates a list that starts at 0 and increases up to the max number plus one
    myList = list(range(0, maxNumber+1))

    #for loop used to iterate through "myList"
    for a in myList:
        print(str(baseNumber) + "*" + str(a) + "=" + str(a*baseNumber))

main()
