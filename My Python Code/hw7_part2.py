#File: hw7_part2.py
#Author: Julio Gamarra
#Date: 4/4/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for part 2 of hw7 for my CMSC 201 class.

USD_TO_BUX_CONVERSION = 8
BUX_TO_USD_CONVERSION = 0.125

#convertToUSD() converts an amount in Retriever Bux to its equivalent amount in U\
S dollars
#Input: amount of Retriever Bux
#Output: equivalent amount in US dollars
def convertToUSD(amount):

    inUSD = amount * BUX_TO_USD_CONVERSION
    return inUSD

#convertToBux() converts an amount in US dollars to its equivalent amount in Retr\
iever Bux
#Input: amount of US dollars
#Output: equivalent amount in Retriever Bux
def convertToBux(amount):

    inBux = amount * USD_TO_BUX_CONVERSION
    return inBux

def main():

    #user menu
    print("Welcome to the Currency Converter")
    print("What would you like to do?")
    print("1. Convert US Dollars to Retriever Bux")
    print("2. Convert Retriever Bux to US Dollars")
    print("3. Exit")

    #asks user to input a choice between 1, 2, or 3
    choice = int(input("Enter your choice: "))
    #while loop to keep asking user for choice if not 1, 2, or 3
    while (choice < 1 or choice > 3):
		print("That is an invalid choice.")
        choice = int(input("Enter your choice: "))

    #condition statements for when to call which function
    if (choice == 1):
        amount = float(input("How much do you want to convert?: "))
        #calls convertToBux function with "amount" as actual parameter
        inBux = convertToBux(amount)
        #formats the output value so that it displays only to 2 decimal places
        inBux = format(inBux, '.2f')
        print(amount, "US dollars equates to", inBux, "Retriever Bux")

    elif (choice == 2):
        amount = float(input("How much do you want to convert?: "))
        #calls convertToUSD function with "amount" as actual parameter
        inUSD = convertToUSD(amount)
        #formats the output value so that it displays only to 2 decimal places
        inUSD = format(inUSD, '.2f')
        print(amount, "Retriever Bux equates to", inUSD, "US dollars")

    print("Good bye, and thank you for using the Currency Converter")

	main()
