#Dominic Colella
#10/31/21
#Lab 7-3 - Dice Game (Not Squid Game)

import random

def main():
    print('This program will ask you to input two names \
and then generate a random number between 1 and \
6 for each. The name of the winner will then \
display.')
    #initialize variables
    endProgram = 'no' or 'n'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'
    #call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo)
    #while loop to run program again
    while endProgram == 'no' or 'n':
        #populate variables
        winnerName = 'NO NAME'
        p1number = 0
        p2number = 0
        #call to roll dice
        winnerName = rollDice(p1number, p2number, playerOne, playerTwo, winnerName)
        #call to display info
        displayInfo(winnerName)
        endProgram = input('Do you want to end the program? Enter yes or no: ')

#player name function
def inputNames(playerOne, playerTwo):
    playerOne = input('Type the name of player One: ')
    playerTwo = input('Type the name of player Two: ')
    return playerOne, playerTwo

#function for random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1,6)
    p2number = random.randint(1,6)
    if p1number > p2number:
        winnerName = playerOne
    elif p2number > p1number:
        winnerName = playerTwo
    elif p2number == p1number:
        winnerName = print('You tied!')
    return winnerName
    
#display winner function
def displayInfo(winnerName):
    print(winnerName)

#calls main
main()