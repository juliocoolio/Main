#File: hw7_part1.py
#Author: Julio Gamarra
#Date: 4/4/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for part 1 of hw7 for my CMSC 201 class.


#convertLetter() converts the letters contained in a string to numbers
#Input: a string (phone number), containing at least one letter
#Output: the new phone number, with all letters changed into numbers
def convertLetter(phoneNumber):

    upAlph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowAlph = "abcdefghijklmnopqrstuvwxyz"

    for i in phoneNumber:
        #for loop to iterate over the range of the english alphabet
        for a in range(len(upAlph)):
            #condition statements for when to replace a letter with which number
            if (i == upAlph[a] or i == lowAlph[a]):
                if (a >= 0 and a <= 2):
                    phoneNumber = phoneNumber.replace(i, "2")
                if (a >= 3 and a <= 5):
                    phoneNumber = phoneNumber.replace(i, "3")
                if (a >= 6 and a <= 8):
                    phoneNumber = phoneNumber.replace(i, "4")
                if (a >= 9 and a <= 11):
                    phoneNumber = phoneNumber.replace(i, "5")
                if (a >= 12 and a <= 14):
                    phoneNumber = phoneNumber.replace(i, "6")
                if (a >= 15 and a <= 18):
                    phoneNumber = phoneNumber.replace(i, "7")
                if (a >= 19 and a <= 21):
                    phoneNumber = phoneNumber.replace(i, "8")
                if (a >= 22 and a <= 25):
                    phoneNumber = phoneNumber.replace(i, "9")

    #assigns the new number after all letters have been changed to numbers
    newNumber = phoneNumber
    return newNumber
	
	

def main():

    print("Welcome to the Telephone Converter")
    #asks user to enter a phone number
    phoneNumber = input("Enter the phone number: ")
    #tests if the phone number the user entered contains all digits
    myBool = phoneNumber.isdigit()

    #condition statement for when to call function
    if (myBool == False):
        newNumber = convertLetter(phoneNumber)
        print(newNumber)
    else:
        print(phoneNumber)

main()

