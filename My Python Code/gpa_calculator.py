#File: gpa_calculator.py
#Author: Julio Gamarra
#Date: 4/7/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for lab 8 of my CMSC 201 class.


def convertLetter(letter):

    if letter == "A":
        return 4
    elif letter == "B":
        return 3
    elif letter == "C":
        return 2
    elif letter == "D":
        return 1
    else:
        return 0


def main():

    grades = open("grades.txt", "r")
    results = open("results.txt", "w")

    for line in grades:
        totalNum = 0
        gradesStrip = line.strip()
        gradesSplit = gradesStrip.split(";")

        for letter in gradesSplit:
            gradeNum = convertLetter(letter)
            totalNum = totalNum + gradeNum
        gpa = totalNum / 3

        output = gradesSplit[0] + " " + gradesSplit[1] + "'s GPA is " + str(gpa)
        print(output)
        results.write(output + "\n")
	
	grades.close()
    results.close()




main()

