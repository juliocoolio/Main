#File: shopping.py
#Author: Julio Gamarra
#Date: 3/10/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for lab5 of my CMSC 201 class.

def main():

    shoppingList = []
    item = ""
    total = 0.0

    while (item != "done"):
        item = input("Add item to list ('done' when finished): ")
        if (item != "done"):
            shoppingList.append(item)
    print("Final shopping list: ", shoppingList)
    print()

    while (shoppingList != []):
        cost = float(input("How much did " + str(shoppingList[0]) + " cost? "))
        total = total + cost
        shoppingList.remove(shoppingList[0])
    print()
    print("Your shopping trip cost $" + str(total))
    print("Shopping list at the end of trip: ", shoppingList)

main()
