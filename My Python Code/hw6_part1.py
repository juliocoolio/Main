#File: hw6_part1.py
#Author: Julio Gamarra
#Date: 3/28/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for part 1 of hw6 for my CMSC 201 class.

def main():

    myList = []
    #for loop to iterate over the desired range of numbers
    for i in range(8):
        #asks user to input a number
        number = int(input("Please enter a number: "))
        p = 0
        #while loop that rechecks the list
        while (p < 10000):
            #for loop that iterates over the list of numbers
            for a in myList:
                #while loop only when user inputs a number already in the list
                while (number == a):
                    print("The number", number, "is already in the list")
                    number = int(input("Please enter a number: "))
            p = p + 1

        #adds the number the user input to the list
        myList.append(number)

    print("The contents of the list are: ")
    #for loop to iterate over the list, printing out the number each time
    for n in myList:
        print(n)


main()
