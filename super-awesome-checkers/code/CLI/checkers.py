# -*- coding: utf-8 -*-
"""
Filename: checker.py
Purpose: Contains the control statements and controls the flow of the game and how the objects relate
Created on Thu Feb 11 21:14:09 2021
@authors: Jake, Ayomide 
Version: 10.0 - 28/5/2021
"""
from setup import piece, board
from algorithm import minimax
import numpy as np
from copy import deepcopy
whiteC=0
blackC=0
#for the undo function
originalPosition=0
currentPosition=0
#Hello world
'''
valid moves are index + 3,4,5 if black pieces
                index +/- 3,4,5 if black kings
                index - 3,4,5 if white pieces
                index +/- 3,4,5 if white kings

The following print statements find if it is a valid move for black or white

print((-int(move[1])+4==-int(move[0])) or (-int(move[1])+5==-int(move[0])) or (-int(move[1])+3==-int(move[0])))
print((-int(move[1])-4==-int(move[0])) or (-int(move[1])-5==-int(move[0])) or (-int(move[1])-3==-int(move[0])))
'''
#Function that changes position on the board
def makeMove(board,turn):
    global currentPosition
    global originalPosition
    #take the move as an input
    mv=input("Enter move in format(11-15, 11x15 for jump): ")
    if 'x' in mv:
        move=mv.split("x")
        try:
            if board[-int(move[0])].checkJump(board)[0]:
                return makeJump(board,turn,move)
            else:
                print("Invalid jump.")
                return makeMove(board, turn)
        except:
            print("Enter move again")
            return makeMove(board,turn)
    move=mv.split("-")
    #use to check the movements of players since the table's outlook does not change
    #possiblePositions = possibleMovements(move,board)
    #print(move)
    #print(board[-int(move[0])].posMoves())
    #print(move)
    #if it is player 1's turn, check if the piece is black and the resulting place is empty
    try:
        if turn==0:
            #Upgrade piece to king, "kb" signifies a promoted piece -Ayo
            if board[-int(move[1])].color==0 and board[-int(move[0])].color=='b' and int(move[1]) in board[-int(move[0])].posMoves():
                
                
                originalPosition=board[-int(move[0])].space
                board[-int(move[1])]=board[-int(move[0])]
                board[-int(move[1])].changeSpace(int(move[1]))
                board[-int(move[0])]=piece(int(move[0]),0)
                print(f"This is current space: { board[-int(move[1])].space }")
                currentPosition=board[-int(move[1])].space
                return board
            else:
                print("Invalid move.")
                return makeMove(board,turn)
        #if it is player 2's turn, check if the piece is white and the resulting place is empty
        else:
            #Promote piece to king, "kw" signifies a promoted piece -Ayo
            if board[-int(move[1])].color==0 and board[-int(move[0])].color=='w' and (int(move[1]) in board[-int(move[0])].posMoves()) :
                
                originalPosition=board[-int(move[0])].space
                board[-int(move[1])]=board[-int(move[0])]
                board[-int(move[1])].changeSpace(int(move[1]))
                board[-int(move[0])]=piece(int(move[0]),0)
                print(f"This is current space: { board[-int(move[1])].space }")
                currentPosition=board[-int(move[1])].space
                return board
            else:
                print("Invalid move.")
                return makeMove(board,turn)
    except:
        print("Enter move again")
        return makeMove(board,turn)

def makeJump(board, turn, move):
    #take the move as an input
    finalLocation=board[-int(move[0])].checkJump(board)[1]
    
    #print(move)
    #print(finalLocation)
    if board[-int(move[1])].color=='w':
        global whiteC
        whiteC += 1
    else:
        global blackC
        blackC += 1
    
    
    board[-int(finalLocation)]=board[-int(move[0])]
    board[-int(finalLocation)].changeSpace(int(finalLocation))
    board[-int(move[0])]=piece(int(move[0]),0)
    board[-int(move[1])]=piece(int(move[0]),0)
    return board       
    
#Initialize the board with values of 0 for 32 spaces
p=board()
#initialize the turn as 0
# 0 is for white and 1 is for black
turn=0

#start the game loop
AIorPerson=input("Do you wanna play with the AI(Input 1) or Another person(Input 2)? ")
print("Black's turn\n\n")
boardSequence = []
sequenceNum=0
boardSequence.append((deepcopy(p),sequenceNum,turn ))
while True:
    #Print the board
    
    
    p.drawP()
    #ask for a move
    if turn==1 and AIorPerson!="1":
        makeMove(p.board,turn)
        print(originalPosition,currentPosition)
        sequenceNum+=1
        boardSequence.append((deepcopy(p),sequenceNum,turn-1 ))
        p.drawP()
        newturn=None
        while True:
            undoQ=input("Do you want to undo the move?(y/n) ")
            if undoQ=="y":
                if len(boardSequence)==1:
                    p=boardSequence[-1][0]
                    newturn = boardSequence[-1][2]
                elif len(boardSequence)>=2:
                    p=boardSequence[-2][0]
                    newturn = boardSequence[-2][2]
                else: 
                    turn=newturn
                    print("You cannot undo any further! ")
                    break
                boardSequence.pop()
                p.drawP()
            elif undoQ=="n":
                if newturn!=None:
                    turn=newturn
                    break
                else:
                    turn=0
                    break
            else:
                break
        
    elif turn==0:
        makeMove(p.board,turn)
        print(originalPosition,currentPosition)
        sequenceNum+=1
        boardSequence.append((deepcopy(p),sequenceNum,turn+1 ))
        
        newturn=None
        while True:
            undoQ=input("Do you want to undo the move?(y/n) ")
            if undoQ=="y" :
                if len(boardSequence)==1:
                    p=boardSequence[-1][0]
                    newturn = boardSequence[-1][2]
                elif len(boardSequence)>=2:
                    p=boardSequence[-2][0]
                    newturn = boardSequence[-2][2]
                else: 
                    turn=newturn
                    print("You cannot undo any further! ")
                    break
                boardSequence.pop()
                p.drawP()
            else:
                if newturn!=None:
                    turn=newturn
                    break
                else:
                    turn=1
                    break
                break
            

        
    else:
        pass
    #Formatting print statements
    print()
    print('-'*10)
    print()
    #Ask if the game should end
    
    if input("Continue playing?(q to quit)")=='q':

        break
    #Formatting print statements
    print()
    print('-'*10)
    print()
    if p.checkWinner()!=None:
        print(f"{ p.checkWinner() } Wins!")
        break
    #Change the turn to the next player's turn
    if turn==1 and AIorPerson=="1":
        value,new_board,finalmove= minimax(p,4,"w")
        print(finalmove[1:3])
        p=new_board[0]
        turn=0
        print("Black's turn\n\n")
    elif turn == 0:
        print("Black's turn\n\n")
    else:
        print("White's turn\n\n")

'''
elif turn==1 and AIorPerson!="1":
        turn=0
        print("Black's turn\n\n")
    else:
        turn=1
        print("White's turn\n\n") '''
