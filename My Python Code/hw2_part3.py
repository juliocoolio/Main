#File: hw2_part3.py
#Author: Julio Gamarra
#Date: 2/15/16
#Lab Section: 09
#UMBC email: jgam1@umbc.edu
#Description: This program is part 3 of hw2 for my CMSC 201 class

def main():

    # introduces the programmer
    print ("Hello, my name is Julio Gamarra")

main()

#Question 12

print ("What is the price? ")
Price = float( input())
dollar = int(Price)
cents = Price - dollar
print ("The number of dollars is: ", dollar)
print ("The number of cents is: ", cents)
