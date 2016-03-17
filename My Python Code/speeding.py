#File: speeding.py
#Author: Julio Gamarra
#Date: 2/25/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the 1st program for lab3 of my CMSC 201 class.

def main():
    #asks user for speed limit
    speedLimit = int(input("Please enter the speed limit in MPH: "))
    #asks user for driving speed
    drivingSpeed = int(input("Please enter the driving speed in MPH: "))
    #calculates by how much the person is speeding
    speeding = drivingSpeed - speedLimit
    #prints by how much the person is speeding
    print("You were over the speed limit by", speeding, "MPH.")

    #conditions for fines
    if (speeding < 5):
        print("You receive no ticket... this time.")
    elif (5 <= speeding <= 15):
        print("You receive a ticket for a $100 fine.")
    elif (15 < speeding < 30):
        print("You receive a ticket for a $200 fine.")
    else:
        print("You receive a ticket for a $500 fine, and a mandatory court date."\
)


main()
