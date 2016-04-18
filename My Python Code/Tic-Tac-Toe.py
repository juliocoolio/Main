#File: proj1.py
#Author: Julio Gamarra
#Date: 4/18/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for project 1 for my CMSC 201 class.

def main():

    again = 1
    while (again == 1):

        #allows the use of random numbers
        import random
        player = random.randint(1,2)
        symbol = random.randint(1,2)

        #condition statements for assigning either "O" or "X" to "symbol"
        if (symbol == 1):
            symbol = "O"
        elif (symbol == 2):
            symbol = "X"

        print()
        print("Welcome to Tic-Tac-Toe")
        print("This is for two players")
        print("Player", player, "will go first and will play with the", symbol)

        #sets up the tic tac toe table
        table = "1|2|3\n-----\n4|5|6\n-----\n7|8|9"
        myString = ""
        print(table)

        #while loop to repeat content until either a winner is determined or all numbers from the table are taken
        while (len(myString) < 9):

            #condition statement to determine a winner
            if ((table[0] == "X" and table[2] == "X" and table[4] == "X") or (table[12] == "X" and table[14] == "X" and table[16] == "X") or (table[24] == "X" and tabl\
e[26] == "X" and table[28] == "X") or (table[0] == "X" and table[12] == "X" and table[24] == "X") or (table[2] == "X" and table[14] == "X" and table[26] == "X") or (ta\
ble[4] == "X" and table[16] == "X" and table[28] == "X") or (table[0] == "X" and table[14] == "X" and table[28] == "X") or (table[4] == "X" and table[14] == "X" and ta\
ble[24] == "X") or (table[0] == "O" and table[2] == "O" and table[4] == "O") or (table[12] == "O" and table[14] == "O" and table[16] == "O") or (table[24] == "O" and t\
able[26] == "O" and table[28] == "O") or (table[0] == "O" and table[12] == "O" and table[24] == "O") or (table[2] == "O" and table[14] == "O" and table[26] == "O") or \
(table[4] == "O" and table[16] == "O" and table[28] == "O") or (table[0] == "O" and table[14] == "O" and table[28] == "O") or (table[4] == "O" and table[14] == "O" and\
 table[24] == "O")):

                print()
                #condition statements used to undo the player switch and symbol switch from the bottom of this while loop
                if (player == 1 and symbol == "O"):
                    player = 2
                    symbol = "X"
                elif (player == 2 and symbol == "X"):
                    player = 1
                    symbol = "O"
                elif (player == 1 and symbol == "X"):
                    player = 2
                    symbol = "O"
                elif (player == 2 and symbol == "O"):
                    player = 1
                    symbol = "X"
                #sets myString to 123456789 in order to skip asking the user for a choice
                myString = "123456789"

            #condition statement to ask user for their choice
            if (myString != "123456789"):
                print()
                print("Player", player, "what is your choice? ")
                choice = int(input("(1-9) or -1 to save or -2 to load: "))
                #while loop to keep asking user, if their number choice is too large or small
                while (choice > 9 or choice == 0 or choice < -2):
                    print()
                    print("Player", player, "what is your choice? ")
                    choice = int(input("(1-9) or -1 to save or -2 to load: "))

            #condition statement for saving the board, symbol, and player
            if (choice == -1):
                save = open("tic.txt", "w")
                save.write(table)
                save.write(str(player))
                save.write(symbol)
				 save.write(myString)
                save.close()
                print("File Saved")
                myString = "123456789"

            #condition statement for loading the board, symbol, and player
            elif (choice == -2):
                save = open("tic.txt", "r")
                readFrom = save.read()
                table = readFrom[0:29]
                myString = readFrom[31:]
                player = int(readFrom[29])
                symbol = readFrom[30]
                print("Game Loaded")
                print(table)
                save.close()

            #condition and for loop to keep asking user, if their number choice is already taken
            elif (myString != "123456789"):
                for i in range(1000):
                    for a in myString:
						 while (a == str(choice)):
                            print()
                            print("That space is already taken.")
                            print("Player", player, "what is your choice? ")
                            choice = int(input("(1-9) or -1 to save or -2 to load: "))
                            #while loop to keep asking user, if their number choice is too large or small
                            while (choice > 9 or choice == 0 or choice < -2):
                                print()
                                print("Player", player, "what is your choice? ")
                                choice = int(input("(1-9) or -1 to save or -2 to load: "))

                            #condition statement for saving the board, symbol, and player
                            if (choice == -1):
                                save = open("tic.txt", "w")
                                save.write(table)
                                save.write(str(player))
                                save.write(symbol)
                                save.write(myString)
                                save.close()
                                print("File Saved")
                                myString = "123456789"
								
                            #condition statement for loading the board, symbol, and player
                            elif (choice == -2):
                                save = open("tic.txt", "r")
                                readFrom = save.read()
                                table = readFrom[0:29]
                                myString = readFrom[31:]
                                player = int(readFrom[29])
                                symbol = readFrom[30]
                                print("Game Loaded")
                                print(table)
                                save.close()

                #for loop to iterate over the table and replace chosen number with X or O and add that number to myString
                for i in table:
                    if (i == str(choice)):
                        table = table.replace(i, symbol)
                        myString = myString + i
                        print(table)

            #if not saving or loading, switches the symbol and player values to the other only options
			 if (choice > 0):
                if (player == 1 and symbol == "O"):
                    player = 2
                    symbol = "X"
                elif (player == 2 and symbol == "X"):
                    player = 1
                    symbol = "O"
                elif (player == 1 and symbol == "X"):
                    player = 2
                    symbol = "O"
                elif (player == 2 and symbol == "O"):
                    player = 1
                    symbol = "X"

            #condition statement for when the 9th number is taken, but the program is still within the loop
            if (len(myString) == 9):

                print()
                #condition statement for determining a winner
                if ((table[0] == "X" and table[2] == "X" and table[4] == "X") or (table[12] == "X" and table[14] == "X" and table[16] == "X") or (table[24] == "X" and \
table[26] == "X" and table[28] == "X") or (table[0] == "X" and table[12] == "X" and table[24] == "X") or (table[2] == "X" and table[14] == "X" and table[26] == "X") or\
 (table[4] == "X" and table[16] == "X" and table[28] == "X") or (table[0] == "X" and table[14] == "X" and table[28] == "X") or (table[4] == "X" and table[14] == "X" an\
d table[24] == "X") or (table[0] == "O" and table[2] == "O" and table[4] == "O") or (table[12] == "O" and table[14] == "O" and table[16] == "O") or (table[24] == "O" a\
nd table[26] == "O" and table[28] == "O") or (table[0] == "O" and table[12] == "O" and table[24] == "O") or (table[2] == "O" and table[14] == "O" and table[26] == "O")\
 or (table[4] == "O" and table[16] == "O" and table[28] == "O") or (table[0] == "O" and table[14] == "O" and table[28] == "O") or (table[4] == "O" and table[14] == "O"\
 and table[24] == "O")):

                    #condition statement for switching the values of player and symbol to the only other options
                    if (player == 1 and symbol == "O"):
                        player = 2
                        symbol = "X"
                    elif (player == 2 and symbol == "X"):
                        player = 1
                        symbol = "O"
                    elif (player == 1 and symbol == "X"):
                        player = 2
                        symbol = "O"
                    elif (player == 2 and symbol == "O"):
                        player = 1
                        symbol = "X"

                    print("Player", player, "with symbol", symbol, "wins!")

                #condition statement for determining a tie
                elif (choice > 0):
                    print("It's a tie!")

                #asks user if he wants to play again
                play = input("Play again? (y or n)?: ")

                #condition statement for playing again
                if (play == "YES" or play == "yes" or play == "y" or play == "Y" or play == "YeS" or play == "yES" or play == "YEs" or play == "yeS" or play == "Yes" o\
r play == "yEs"):
                    again = 1

                #condition statement for not playing again
                elif (play == "NO" or play == "no" or play == "n" or play == "N" or play == "No" or play == "nO"):
                    again = 0
                    print("Thank you for playing")
					

main()

