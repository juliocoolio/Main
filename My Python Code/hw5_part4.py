#File: hw5_part4.py
#Author: Julio Gamarra
#Date: 3/8/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for part 4 of hw5 for my CMSC 201 class.

def main():

    print("Welcome to the Extra Credit Challenge!!!")
    #asks user to input number of points
    numPoints = int(input("Enter the number of points to play for (13-21): "))
    numPointsOne = 0
    numPointsTwo = 0
    turnOne = 0
    turnTwo = 0

    #while loop to keep asking for right range of points
    while (numPoints > 21 or numPoints < 13):
        print("Error: You can play for 13-21 points")
        numPoints = int(input("Enter the number of points to play for (13-21): "))
    print()
    print("Player 2 starts")

    #while loop to keep going until number of points reaches 0
    while (numPoints > 0):
        #condition for when 3 or more points remaining
        if (numPoints >= 3):
            print("There are", numPoints, "points left.")
            takePointsTwo = int(input("Player 2, how many points do you take? (1-3): "))
            print()
            while (takePointsTwo > 3 or takePointsTwo < 1):
                print("Error: You can take 1-3 points")
                takePointsTwo = int(input("Player 2, how many points do you take? (1-3): "))
                print()
            #updates number of points for player 2
            numPointsTwo = numPointsTwo + takePointsTwo
            #updates remaining number of points
            numPoints = numPoints - takePointsTwo
            if (numPoints >= 3):
                print("There are", numPoints, "points left.")
				 takePointsOne = int(input("Player 1, how many points do you take? (1-3): "))
                while (takePointsOne > 3 or takePointsOne < 1):
                    print("Error: You can take 1-3 points")
                    takePointsOne = int(input("Player 1, how many points do you take? (1-3): "))
                    print()
                #updates number of points for player 1
                numPointsOne = numPointsOne + takePointsOne
                #updates remaining number of points
                numPoints = numPoints - takePointsOne
                print()

        #condition for when 2 points remaining
        elif (numPoints == 2):
            print("There are", numPoints, "points left.")
            takePointsTwo = int(input("Player 2, how many points do you take? (1-2): "))
            while (takePointsTwo > 2 or takePointsTwo < 1):
                print("Error: You can take 1-2 points")
                takePointsTwo = int(input("Player 2, how many points do you take? (1-2): "))
            #updates number of points remaining
            numPoints = numPoints - takePointsTwo
            #updates remaining number of points for player 2
			 numPointsTwo = numPointsTwo + takePointsTwo
            print()
        #condition for when 1 point remaining
        elif (numPoints == 1):
            print("There are", numPoints, "points left.")
            takePointsTwo = int(input("Player 2, how many points do you take? (1): "))
            while (takePointsTwo != 1):
                print("Error: You can take 1 point")
                takePointsTwo = int(input("Player 2, how many points do you take? (1): "))
            #updates number of points remaining
            numPoints = numPoints - takePointsTwo
            #updates number of points for player 2
            numPointsTwo = numPointsTwo + takePointsTwo
            print()


    if (numPoints <= 0):
        if (numPointsOne > numPointsTwo):
            print("Congratulations! Player 1 has won!!!")
        elif (numPointsTwo > numPointsOne):
            print("Congratulations! Player 2 has won!!!")
			        elif (numPointsOne == numPointsTwo):
            print("The game was a draw!")

main()
