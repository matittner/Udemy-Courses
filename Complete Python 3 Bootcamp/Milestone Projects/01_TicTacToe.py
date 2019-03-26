"""
Mateus H Ittner - 23/08/18
Udemy - "Complete Python 3 Bootcamp"

Milestone Project 1 - Tic Tac Toe
"""
from os import name,system # for clearing the console
from random import randint
from time import sleep

def clear():
	"""
	Clear the output screen
	"""
    # for windows
	if name == 'nt':
		system('cls')

    # for mac and linux(here, os.name is 'posix')
	else:
		system('clear')

def displayBoard(board):
	"""
	Takes a list with 9 char and print out the board with the positions and the current board
	Positions follow a numpad configuration (-1 cause indexing ofc)
	[7][8][9]
	[4][5][6]
	[1][2][3]
	"""
	clear()
	print(f" 7 | 8 | 9		 {board[6]} | {board[7]} | {board[8]} ")	#   |   |   
	print("-----------		-----------")								#-----------
	print(f" 4 | 5 | 6		 {board[3]} | {board[4]} | {board[5]} ")	#   |   |   
	print("-----------		-----------")								#-----------
	print(f" 1 | 2 | 3		 {board[0]} | {board[1]} | {board[2]} ")	#   |   |   

def checkWin(board):
	"""
	Takes a list with 9 char and checks if there's a winning sequence or if's a tie 
	Returns the winning char, 't' if full (tie). Else returns ' '
	"""

	if board[0] == board[1] == board[2] != ' ':		#Bottom horizontal
		return board[0] 
	elif board[3] == board[4] == board[5] != ' ':	#Middle horizontal
		return board[3]
	elif board[6] == board[7] == board[8] != ' ':	#Top horizontal
		return board[6]
	elif board[0] == board[3] == board[6] != ' ':	#Left vertical
		return board[0]
	elif board[1] == board[4] == board[7] != ' ':	#Middle vertical
		return board[1]
	elif board[2] == board[5] == board[8] != ' ':	#Right vertical
		return board[2]
	elif board[6] == board[4] == board[2] != ' ':	#1st diagonal
		return board[6]
	elif board[0] == board[4] == board[8] != ' ':	#2nd diagonal
		return board[0]

	if not ' ' in board:	# if there isn't a winner and no empty spaces left
		return 't'
	else:
		return ' '			# no winners but not full yet

def pickPosition(board,player):
	"""
	Takes a list with 9 char (board) and the current player (char)
	Returns the list with the new picked position
	"""

	while True:
		while True:
			displayBoard(board)
			try:
				position = int(input(f"Player '{player}', pick a position: "))
			except:
				print("Pick a number!")
				sleep(1)
			else:
				break
		if board[position-1] != ' ':
			print("Pick an empty position!")
			sleep(1)
		else:
			board[position-1] = player
			break
	
	return board


newgame = 'y'

while newgame.lower() != 'n':
	board = [' '] * 9	# empty board

	player1 = input("Player 1, pick a character: ").upper()
	while True:
		player2 = input("Player 2, pick a character: ").upper()
		if player2 == player1:
			print("Can't be the same as player 1!")
		else:
			break

	boardstatus = ' ' # holds the board status, received from checkWin()

	if randint(0,1) == 1:	# picks a random starting player
		print("Player 1 starts!")
		lastturn = player2	# last turn was player 2
	else:
		print("Player 2 starts!")
		lastturn = player1	# last turn was player 1

	while boardstatus == ' ':	#while not full and noone won
		
		if lastturn == player1:
			print("Player 2, your turn: ")
			sleep(1)
			board = pickPosition(board,player2)	# player picks a position and pass the turn
			lastturn = player2
		else:
			print("Player 1, your turn: ")
			sleep(1)
			board = pickPosition(board,player1)
			lastturn = player1

		boardstatus = checkWin(board) # check if the last move won or if it's a tie

	displayBoard(board)
	if boardstatus == player1:
		print("Player 1 won!")
	elif boardstatus == player2:
		print("Player 2 won!")
	else:
		print("It's a tie!")

	newgame = input("Play again? (Y/N) ")
