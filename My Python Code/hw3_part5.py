#File: hw3_part5.py
#Author: Julio Gamarra
#Date: 2/22/16
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for part 5 of hw3 for my CMSC 201 class.

def main():

    #asks user for day of the month
    dayOfMonth = int(input("What day of the month is it? "))
    #checks for input numbers between 1 and 31
    if 1 <= dayOfMonth <= 31:
        #calculates the remainder
        dayOfWeek = dayOfMonth % 7
        #uses the remainder to indicate day of week
        if dayOfWeek == 0:
            print("Today is Sunday!")
        elif dayOfWeek == 1:
            print ("Today is Monday!")
        elif dayOfWeek == 2:
            print ("Today is Tuesday!")
        elif dayOfWeek == 3:
            print ("Today is Wednesday!")
        elif dayOfWeek == 4:
            print ("Today is Thursday!")
        elif dayOfWeek == 5:
            print ("Today is Friday!")
        elif dayOfWeek == 6:
            print ("Today is Saturday!")

    else:
        #error message for when input number isn't between 1 and 31
        print ("Invalid Day")

main()
