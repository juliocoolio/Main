#File: hw5_part1.py
#Author: Julio Gamarra
#Date: 3/8/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for part 1 of hw5 for my cmsc 201 class.

def main():
    #asks user to input bill
    totalBill = float(input("What is the total bill? "))
    excellentTip = 0.25
    goodTip = 0.20
    badTip = 0.10
    minimum = 2

    print("What was the level of service? ")
    #asks user to input level of service
    levelService = input("(Please choose excellent, good, or bad): ")
    #while loop to repeat service question
    while (levelService != "excellent" and levelService != "good" and levelService != "bad"):
        print("What was the level of service? ")
        levelService = input("(Please choose excellent, good, or bad): ")

    print("The bill was $" + str(totalBill))
    print("The service was", levelService)

    #conditions for calculations
    if (levelService == "excellent"):
        tip = excellentTip * totalBill
    elif (levelService == "good"):
        tip = goodTip * totalBill
    elif (levelService == "bad"):
        tip = badTip * totalBill

    if (tip < minimum):
        tip = minimum

    print("The tip is $" + str(tip))
    #calculates the grand total bill
    grandTotal = tip + totalBill
    print("The grand total with tip is $" + str(grandTotal))

main()