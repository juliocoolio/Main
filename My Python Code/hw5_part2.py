#File: hw5_part2.py
#Author: Julio Gamarra
#Date: 3/8/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for part 2 of hw5 for my CMSC 201 class.

def main():

    firstHundred = 0.08
    nextNineHundred = 0.06
    nextNineThousand = 0.05
    afterTenThousand = 0.04

    hundred = 100
    nineHundred = 900
    thousand = 1000
    nineThousand = 9000
    tenThousand = 10000
    #asks user to input number of copies
    copies = int(input("How many copies do you want? "))

    #conditions for the cost per copy based on amount
    if (copies <= 100):
        totalCost = copies * firstHundred
        print("The total cost for", copies, "copies is $" + str(totalCost))
    elif (100 < copies <= 1000):
        totalCost = hundred * firstHundred + (copies - hundred) * nextNineHundred
        print("The total cost for", copies, "copies is $" + str(totalCost))
    elif (1000 < copies <= 10000):
        totalCost = hundred * firstHundred + nineHundred * nextNineHundred + (copies - thousand) * nextNineThousand
        print("The total cost for", copies, "copies is $" + str(totalCost))
    elif (10000 < copies):
        totalCost = hundred * firstHundred + nineHundred * nextNineHundred + nineThousand * nextNineThousand + (copies - tenThousand) * afterTenThousand
        print("The total cost for", copies, "copies is $" + str(totalCost))

main()
