#File: hw6_part3.py
#Author: Julio Gamarra
#Date: 3/28/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for part 3 of hw6 for my CMSC 201 class.


#drawSquare() draws a square made of asteriks from the number the user inputs
#Input: the size of the square
#Output: square shape made of asteriks
def drawSquare(size):
    p = 1
    while (p <= size):
        s = 1
        while (s <= size):
            print("*", end = "")
            s = s + 1
        print()
        p = p + 1


#drawTriangle() draws a triangle made of asteriks from the number the user inputs
#Input: the size of the triangle
#Output: triangle shape made of asteriks
def drawTriangle(size):
    p = 1
    while (p <= size):
        print("*" * p)
        p = p + 1


#drawParallelogram() draws a parallelogram made of asteriks from the number the u\
ser inputs
#Input: the size of the parallelogram
#Output: parallelogram shape made of asteriks
def drawParallelogram(size):
    p = 1
    while (p <= size):
        s = 1
        while (s <= size):
			print("*" * p)
			p = p + 1


#drawParallelogram() draws a parallelogram made of asteriks from the number the u\
ser inputs
#Input: the size of the parallelogram
#Output: parallelogram shape made of asteriks
def drawParallelogram(size):
    p = 1
    while (p <= size):
        s = 1
        while (s <= size):
            print("*", end = "")
            s = s + 1
        if (p != size):
            print()
            print(end = " " * p)
        p = p + 1
    print()



def main():

    #asks user to input a positive integer
    number = int(input("Please enter a positive integer: "))
    #while loop to keep asking for when user inputs negative integer or 0
    while (number < 1):
        number = int(input("Please enter a positive integer: "))

    #asks user to input shape name
    shape = input("Please choose the shape: square, parallelogram, triangle, or all: ")
    #while loop to keep asking for when user does not input name from the printed options
    while (shape != "triangle" and shape != "parallelogram" and shape != "square" and shape != "all"):
        shape = input("Please choose the shape: square, parallelogram, triangle, or all: ")

    #condition statements for which function(s) to call
    if (shape == "square"):
        drawSquare(number)
    elif (shape == "triangle"):
        drawTriangle(number)
    elif (shape == "parallelogram"):
        drawParallelogram(number)
    elif (shape == "all"):
        drawSquare(number)
        print()
        drawParallelogram(number)
        print()
		drawTriangle(number)

main()

