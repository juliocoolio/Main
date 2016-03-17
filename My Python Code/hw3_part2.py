#File: hw3_part2.py
#Author: Julio Gamarra
#Date: 2/22/16
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is a program for part 2 of hw3 for my CMSC 201 class.

def main():
    #asks user to input grades and weights
    hwWeight = float(input("What is the homework weight? "))
    hwGrade = float(input("What is the homework grade? "))
    examWeight = float(input("What is the exam weight? "))
    examGrade = float(input("What is the exam grade? "))
    discussionWeight = float(input("What is the discussion weight? "))
    discussionGrade = float(input("What is the discussion grade? "))
    #calculates the total grade
    weightedTotal = (hwWeight * hwGrade) + (examWeight * examGrade) + (discussionWeight * discussionGrade)
    #tells user the numerical grade
    print ("The final numerical grade is", weightedTotal)
    #tells user the letter grade
    if weightedTotal >= 90:
        print ("This earns you an A in the class.")
    if 89.9 >= weightedTotal >= 80:
        print ("This earns you a B in the class.")
    if 79.9 >= weightedTotal >= 70:
        print ("This earns you a C in the class.")
    if 69.9 >= weightedTotal >= 60:
        print ("This earns you a D in the class.")
    if 59.9 >= weightedTotal >= 0:
        print ("This earns you an F in the class.")


main()
