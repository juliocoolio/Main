#File: hw2_part2.py
#Author: Julio Gamarra
#Date: 2/15/16
#Lab Section: 09
#UMBC email: jgam1@umbc.edu
#Description: This program is part 2 of hw2 for my CMSC 201 class.

def main():

    #introduces the programmer
    print ("Hello, my name is Julio Gamarra")

main()


#Question 11

BookPrice = float(input("What is the price of the book? "))
NumBooks = float(input("How many copies of this book would you like? "))
Tax = 0.065 * BookPrice * NumBooks
ShippingCharge = NumBooks * 1.95
TotalCost = Tax + ShippingCharge + BookPrice*NumBooks
print ("The total cost of the order is", TotalCost)
