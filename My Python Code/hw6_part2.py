#File: hw6_part2.py
#Author: Julio Gamarra
#Date: 3/28/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for part 2 of hw6 for my CMSC 201 class.

def main():

    #initializes myList as the set of numbers between 2 and 500, included
    myList = list(range(2, 501))
    n = 2

    #while loop that repeats its contents for numbers 2 through 25, included
    while (n <= 25):
        #for loop to iterate through myList
        for i in myList:
            #condition statement for when to remove number from myList
            if (i % n == 0 and i != n):
                myList.remove(i)
        n = n + 1

    #for loop to iterate through myList and print out the numbers in one line
    for i in myList:
        print(i, end = " ")
    print()



main()
