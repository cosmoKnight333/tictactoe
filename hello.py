import random
import numpy
from numpy.core.defchararray import isnumeric
choices = []
numbers = []
for x in range (0, 9) :
    choices.append(" ")
    numbers.append(x)


def ifdraw():
    c=True
    for i in choices:
        if i==' ':
            c=False
    return c
        

def printTable() :

    print( '_' + choices[0] + '_|_' + choices[1] + '_|_' + choices[2] + '_'+"     "+'_' + '1' + '_|_' + '2' + '_|_' + '3' + '_')
    print( '_' + choices[3] + '_|_' + choices[4] + '_|_' + choices[5] + '_'+" <-> "+'_' + '4' + '_|_' + '5' + '_|_' + '6' + '_')
    print( ' ' + choices[6] + ' | ' + choices[7] + ' | ' + choices[8] +    "      "+' ' + '7'+ ' | ' + '8' + ' | ' + '9' + ' ' +' \n')

def checkWinn():
    if choices[0]=='X' and choices[1]=='X' and choices[2]=='X' or choices[3]=='X' and choices[4]=='X' and choices[5]=='X' or  choices[6]=='X' and choices[7]=='X' and choices[8]=='X':
        return 1
    if choices[0]=='X' and choices[3]=='X' and choices[6]=='X' or choices[1]=='X' and choices[4]=='X' and choices[7]=='X' or  choices[2]=='X' and choices[5]=='X' and choices[8]=='X':
        return 1
    if choices[0]=='X' and choices[4]=='X' and choices[8]=='X' or choices[2]=='X' and choices[4]=='X' and choices[6]=='X' :
        return 1
    if choices[0]=='O' and choices[1]=='O' and choices[2]=='O' or choices[3]=='O' and choices[4]=='O' and choices[5]=='O' or  choices[6]=='O' and choices[7]=='O' and choices[8]=='O':
        return 2
    if choices[0]=='O' and choices[3]=='O' and choices[6]=='O' or choices[1]=='O' and choices[4]=='O' and choices[7]=='O' or  choices[2]=='O' and choices[5]=='O' and choices[8]=='O':
        return 2
    if choices[0]=='O' and choices[4]=='O' and choices[8]=='O' or choices[2]=='O' and choices[4]=='O' and choices[6]=='O' :
        return 2
    if ifdraw():
        return 0

def multiplayer():
    playerOneTurn=True
    while 1:
        printTable()

        if playerOneTurn :
            print( "Player 1:")
            inp=input()
            if isnumeric(inp) :
                a = int(inp)
                if a in range(1,10) and choices[a - 1] == ' ':
                    choices[a - 1] = 'X'
                    playerOneTurn = False
                else:
                    print("Ivalid move")
            else:
                print("Ivalid move")

        else :
            print( "Player 2:")
            inp=input()
            if isnumeric(inp) :
                a = int(inp)
                if a in range(1,10) and choices[a - 1] == ' ':
                    choices[a - 1] = 'O'
                    playerOneTurn = True
                else:
                    print("Ivalid move")
            else:
                print("Ivalid move")

        if checkWinn()==1:
                print("Player 1 wins!!")
                break
        if checkWinn()==2:
                print("Player 2 wins!!")
                break
        if checkWinn()==0:
                print("Match draw!!")
                break
    printTable()    



def playerOne():
    playerOneTurn=True
    while 1 :
        printTable()

        if playerOneTurn :

            print( "Your Chance:")
            inp=input()
            if isnumeric(inp) :
                a = int(inp)
                if a in range(1,10) and choices[a - 1] == ' ':
                    choices[a - 1] = 'X'
                    playerOneTurn = False
                else:
                    print("Ivalid move")
            else:
                print("Ivalid move")
            
        else :
            print( "CPU's Chance:")
            #INP A RANDON NO. IN THE NON SELECTED ARRAY
            arra=[]
            for i in range(9):
                if choices[i] ==' ':
                    arra.append((int(i)+1))
            inp= random.choice(arra)
            print(inp)
            choices[inp - 1] = 'O'
            playerOneTurn = True
            
        if checkWinn()==1:
            print("You win!!")
            break
        if checkWinn()==2:
            print("CPU wins!!")
            break
        if checkWinn()==0:
            print("Match draw!!")
            break
    printTable()
def playerTwo():
    playerOneTurn=True

    while 1 :
        printTable()

        if playerOneTurn :
            print( "CPU's Chance:")
            #INP A RANDON NO. IN THE NON SELECTED ARRAY
            arra=[]
            for i in range(9):
                if choices[i] ==' ':
                    arra.append((int(i)+1))
            inp= random.choice(arra)
            print(inp)
            choices[inp - 1] = 'X'
            playerOneTurn = False
        
            
        else :
            print( "Your Chance:")

            inp=input()
            if isnumeric(inp) :
                a = int(inp)
                if a in range(1,10) and choices[a - 1] == ' ':
                    choices[a - 1] = 'O'
                    playerOneTurn = True
                else:
                    print("Ivalid move")
            else:
                print("Ivalid move")
            playerOneTurn=True
        if checkWinn()==1:
            print("CPU wins!!")
            break
        if checkWinn()==2:
            print("You win!!")
            break
        if checkWinn()==0:
            print("Match draw!!")
            break
    printTable()

k=input("For single Player press s for multiplayer press m :")
if k=='m':
    multiplayer()
else:
    p=input("To play as Player One press 1 or player Twos press 2 :")
    if p=='1':
        playerOne()
    else:
        playerTwo()