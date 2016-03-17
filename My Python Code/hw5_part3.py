#File: hw5_part3.py
#Author: Julio Gamarra
#Date: 3/8/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Decription: This is the program for part 3 of hw5 for my CMSC 201 class.

def main():
    #asks user to input phone number
    phoneNumber = input("Please enter the phone number: ")
    #calculates length of phone number
    length = len(phoneNumber)

    #conditions for rearranging the phone number into proper format
    if (phoneNumber[0] == "(" and phoneNumber[4] == ")" and phoneNumber[8] == "-"):
        print("The formatted phone number is:", phoneNumber[0:5], phoneNumber[5:length])
    elif (phoneNumber[3] == "-" and phoneNumber[7] == "-"):
        print("The formatted phone number is:", "(" + phoneNumber[0:3] + ")", phoneNumber[4:length])
    else:
        print("The formatted phone number is:", "(" + phoneNumber[0:3] + ")", phoneNumber[3:6] + "-" + phoneNumber[6:length])




main()
