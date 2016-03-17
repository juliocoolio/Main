#File: hw3_part3.py
#Author: Julio Gamarra
#Date: 2/22/16
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is a program for part 3 of hw3 for my CMSC 201 class.

def main():

    #asks user if the character is a woman or not
    woman = str(input("Is the character a woman? "))
    if woman == "y":
        #asks user if the character has blue eyes or not
        blueEyes = str(input("Does the character have blue eyes? "))
        if blueEyes == "y":
            print ("Your character is Jane.")
        else:
            print ("Your character is Marni.")
    elif woman == "n":
        #asks user if the character has glasses or not
        glasses = str(input("Does the character wear glasses? "))
        if glasses == "y":
            print ("Your character is Adrian.")
        elif glasses == "n":
            #asks user if the character has a beard or not
            beard = str(input("Does your character have a beard? "))
            if woman == "n" and glasses == "n" and beard == "y":
                print ("Your character is Peder.")
            else:
                print ("Your character is Zhang.")

main()
