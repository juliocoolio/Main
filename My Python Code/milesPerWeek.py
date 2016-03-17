#File: milesPerWeek.py
#Author: Julio Gamarra
#Date: 2/18/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is my program for lab 02 of my CMSC 201 class

MilesPerHour = 65
OneWay = float(input("How many miles do you drive each way to work? "))
DaysPerWeek = int(input("How many days do you drive to work each week? "))
MilesPerWeek = OneWay * 2 * DaysPerWeek
HoursPerWeek = MilesPerWeek / MilesPerHour
print("You drive", MilesPerWeek, "miles per week.")
print("At 65 mph, you spend", HoursPerWeek, "hours commuting in the car each week\
.")
