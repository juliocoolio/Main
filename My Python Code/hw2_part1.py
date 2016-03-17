#File: hw2_part1.py
#Author: Julio Gamarra
#Date: 2/15/16
#Lab Section: 09
#UMBC email: jgam1@umbc.edu
#Description: This program is part 1 of hw2 for my CMSC 201 class.

def main():

    #introduces the programmer
    print ("Hello, my name is Julio Gamarra")

main()

#Question 1
#Expected output: 55
num1 = (7 + 4) * 5
print("Question 1 evaluates to:", num1)
#Actual output: 55
#Explanation: Parentheses first (11), then multiplication (55)

#Question 2
#Expected output: 1
num2 = (15 % 7)
print ("Question 2 evaluates to:", num2)
#Actual output: 1
#Explanation: Parentheses (1)

#Question 3
#Expected output: 0
num3 = (32 % 36)
print ("Question 3 evaluates to:", num3)
#Actual output: 32
#Explanation: Parentheses (32), I thought it was 0 because 36 goes into 32 zero times# but I forgot to count the remaining amount.

#Question 4
#Expected output: 12
num4 = (5 - 3) + (10 - 5) * (8 % 3)
print ("Question 4 evaluates to:", num4)
#Actual output: 12
#Explanation: Parentheses first (2, 5, 2), then multiplication (10), then addition (12#)
