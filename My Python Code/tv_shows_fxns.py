# File:    tv_shows_fxns.py
# Author:  Julio Gamarra
# Date:    3/31/16
# Section: 09
# E-mail:  jgam1@umbc.edu
# Description:
#   This file contains python code that implements lab6 (a
#   TV show voting system) using functions to:
#   1) Get a choice
#   2) Find the name of the winner

STOP = 0

# getVote() returns a valid choice from the given list
# Input:    showList, a list of strings (names of shows to vote on)
# Output:   vote,     an integer containing a choice between 0 and list length
#          *reprompts user until valid choice is made*
def getVote(showList):

    vote = int(input("Enter '0' to stop voting: "))
    while (vote != 0 and (vote < 1 or vote > len(showList))):
        print("Invalid vote -- try again")
        vote = int(input("Enter '0' to stop voting: "))
    return vote


# getWinner() takes in a list of shows and votes and calculates the winner
# Input:      showList, a list of strings (names of shows to vote on)
#             votes,    a list of integers (votes for each show)
# Output:     whoWon,   the name of the show that won with the most votes
#             *in case of a tie, the first show seen in the list wins*
def getWinner(showList, votes):

    winnerVote = -1
    for i in range(len(showList)):
        if (votes[i] > winnerVote):
            winnerVote  = votes[i]
            whoWon = showList[i]
    return whoWon
	
def main():

    # initialize shows and votes lists, and choice variable
    shows  = ["Daredevil", "Fargo",
              "Limitless", "Elementary", "Brooklyn 99",
              "Empire", "Supergirl"]
    votes  = [0]*len(shows)
    choice = 1

    # print the voting number and show name
    for i in range(len(shows)):
        print(i + 1, "-", shows[i])
    # print the program greeting/instructions
    print("You and your friends are voting on a show to watch.")
    print("Which show would you like to vote for?")

    while choice != STOP:

        choice = getVote(shows)
        if (choice != 0):
            votes[choice - 1] = votes[choice - 1] + 1
		
	 # once done voting, print the results
    print("\nHere are the final votes:")
    for i in range(len(shows)):
        print(shows[i], "has\t", votes[i], "votes")

    winner = getWinner(shows, votes)

    print(winner, "wins!")

main()


