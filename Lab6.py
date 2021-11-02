#Dom Colella
#10/25/21
#Calculatin' how good at recycling humanity is

#Lab 6 The Bottle Return Program

#the main function
def main():
    endProgram = 'n'
    while endProgram == 'n':
        totalBottles = getBottles()
        totalPayout = calcPayout(totalBottles)
        printInfo(totalBottles, totalPayout)
        endProgram = input('Do you want to end the program? (Enter y or n): ')
        
#This prompts the user to enter the total bottles returned in a week        
def getBottles():
    totalBottles = 0
    todayBottles = 0
    counter = 1
    while counter <= 7:
        todayBottles = int(input('Enter the number of bottles returned today: '))
        totalBottles = totalBottles + todayBottles
        counter += 1
    return totalBottles

#this lil' function calculates payout
def calcPayout(totalBottles):
    totalPayout = 0
    totalPayout = totalBottles * .10
    return totalPayout

#now we find out if we did good at recycling
def printInfo(totalBottles, totalPayout):
    print('The total number of bottles returned is', totalBottles)
    print('The total paid out is $', float(totalPayout))

#Calls main
main()
