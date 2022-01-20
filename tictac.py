#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 16:16:37 2021

@author: poorvajuneja
"""

'''
TIC TAC TOE BOARD 
[
 [-,-,-]
 [-,-,-]
 [-,-,-]
 
 ]
USER_INPUT-->SOMETHING 1-9
if they enter anything else: tell them to go again
check if the the user_input is already taken
add it th the board
check if user won: checking rows,colums and diagnols

toggle between users moves

'''
board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-'],
 
    ]

user = True #when true it refers to x,otherwise o
turn = 0

def print_board(board):
   #iterating 2D list 
    for row in board:
        for slot in row:
             print(f'{slot} ', end='')
        print()
def quit_game(user_input):
    if user_input.lower() == 'q':
        print('Thanks for playing')
        return True
         
    else:
        return False
    
def check_input(user_input):
    #check if its a number
    if not isnum(user_input):
        return False
    user_input = int(user_input)
    #check if its 1-9
    if not bounds(user_input):
        return False
    else:
          return True
    
def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print('This number is out of bounds')
        return False
    else:
        return True
        
    
def isnum(user_input):
    if not user_input.isnumeric():
        print('This is not a valid number')
        return False
    else:
        return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != '-':
        print('This position is already taken')
        return True
    else:
        return False    
    
def coordinates(user_input):
    row = int(user_input) // 3
    col = int(user_input)#----?
    if col > 2:
        col = int(col % 3)
    return (row,col)

def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user
     

def current_user(user):#question?
    if user:
        return 'x'
    else:
        return 'o'


def checkRow(user, board):
    for row in board:
        complete_row = True#set booloean to check
        for slot in row:
            if slot != user:#????
                complete_row = False
                break
        if complete_row:
            return True
    return False#?????
                

def checkColumn(user,board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break#break out of inner loop 
        if complete_col:
            return True
    return False#iterate through and doesnt find a complete column 

def checkDiag(user,board):
    if board [0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board [2][0] == user:
        return True
    else:
        return False                

def isWin(user,board):
    if checkRow(user,board):
        return True
    if checkColumn(user, board):
        return True
    if checkDiag(user, board):
        return True
    else:
        return False #default it will
    
    
while turn < 9:
   active_user = current_user(user)
   print_board(board)
   user_input = input('please enter a position through 1 to 9 or enter \'q\' to quit') 
   if quit_game(user_input):
       break   
   if not check_input(user_input):
      print('Please try again') 
      continue  #goes up to begining doesnt proceed down   
   user_input = int(user_input)-1 
   coords = coordinates(user_input)
   if istaken(coords,board):
       print('Please try again.')
       continue#goes up to begining doesnt proceed down
   add_to_board(coords, board,active_user)
   if isWin(active_user,board):
       print(f'{active_user.upper()} won!')
       break
   turn += 1
   if turn == 9:
        print('It\'s a tie')
   user = not user
       
       
