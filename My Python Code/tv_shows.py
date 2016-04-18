#File: tv_shows.py
#Author: Julio Gamarra
#Date: 3/24/2016
#Section: 09
#E-mail: jgam1@umbc.edu
#Description: This is the program for lab6 for my CMSC 201 class.


def main():

    shows = ["Daredevil", "Fargo", "Limitless", "Elementary", "Brooklyn 99", "Emp\
ire", "Supergirl"]
    for i in range(len(shows)):
        print(i + 1, "-", shows[i])
    print("You and your friends are voting on a show to watch.")
    print("Which show would you like to vote for?")
    vote = 1
    votesList = [0, 0, 0, 0, 0, 0, 0]
    while (vote != 0):
        vote = int(input("Enter '0' to stop voting: "))
        if (vote >= 1 and vote <=7):
            votesList[vote - 1] = votesList[vote - 1] + 1
    print()
    print("Here are the final votes:")
    for i in range(len(shows)):
        print(shows[i], "has\t", votesList[i], "votes")


    winnerVote = -1
    winner = ""
    tie = 0
    a = 0
    for i in range(len(votesList)):
        if (votesList[i] > winnerVote):
            winnerVote = votesList[i]
            winner = shows[i]
            a = i
    votesList.remove(votesList[a])
    for i in range(len(votesList)):
        if (winnerVote == votesList[i]):
            tie = 1
    if (tie == 1):
		print("It's a tie!")
    else:
        print("The winner is", winner, "with", winnerVote, "votes.")
main()
