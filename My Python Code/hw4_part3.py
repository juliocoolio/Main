#File: hw4_part3.py
#Author: Julio Gamarra
#Date: 2/29/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is a program for part 3 of hw4 for my CMSC 201 class.

def main():

    #asks user to input the number of pledges
    pledges = int(input("How many pledges did you get? "))
    #creates a list starting at 1 and ending at the number of pledges, included
    myList = list(range(1, pledges + 1))
    totalValue = 0

    #for loop used to iterate through "myList"
    for a in myList:
        #asks user to input values for all donations
        string = input("What is the value of donation " + str(a) + ": ")
        #adds the donation value from this iteration to the "totalValue"
        totalValue = totalValue + float(string)

    #asks user to input the number of plunges
    plunges = int(input("How many plunges did you do? "))
    #calculates the total amount earned
    totalDonation = totalValue * plunges
    print("Based on your", plunges, "plunges your earned $" + str(totalDonation), "for the charity.")


main()
