#File: speeding.py
#Author: Julio Gamarra
#Date: 2/25/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the 2nd program for lab3 for my CMSC 201 class.

def main():
    #asks user for to input a word
    word = input("Please enter a word: ")

    #condition for manners or lack of manners
    if (word == "please" or word == "thank you" or word == "excuse me"):
        print("Your manners are impeccable.")
    else:
        print("How rude!")

main()
