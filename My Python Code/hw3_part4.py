#File: hw3_part4.py
#Author: Julio Gamarra
#Date: 2/22/16
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This program is part 4 of hw3 for my CMSC 201 class.

def main():
    #asks user to input the temperature
    temperature = float(input("What is the temperature? "))
    #verifies the scale being used
    scale = str(input("Enter 'C' for Celsius, or 'F' for Fahrenheit: "))
    #converts the Farenheit temperature to Celsius temperature
    if scale == "F":
        temperature = (temperature - 32) * 5/9
    if temperature >= 100:
        print("At this temperature, water is a gas.")
    if 0 <= temperature < 100:
        print ("At this temperature, water is a liquid.")
    if temperature < 0:
        print("At this temperature, water is frozen.")

main()
