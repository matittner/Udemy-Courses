"""
Mateus H Ittner - 23/08/18
Udemy - "Complete Python 3 Bootcamp"

Milestone Project 2 - Blackjack
"""

from random import shuffle
from os import system, name
from time import sleep

def cls():
	"""
	Clear output
	"""
	if name == 'nt':
		system('cls')
	else:
		system('clear')

class Card():
	"""
	Class for a card, takes a str suit (ex hearts) and a str rank (one, seven)
	"""

	values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __repr__(self):
		return f"{self.rank} of {self.suit}"

	def __eq__(self,rank):
		return rank == self.rank


class Deck():
	"""
	Class for the deck of cards, takes a list of Card
	"""
	def __init__(self, cards):
		self.cards = cards

	def __repr__(self):
		return str(self.cards)

	def shuffleDeck(self):
		"""
		Randomly shuffles the deck
		"""
		shuffle(self.cards)

	def pickCard(self):
		"""
		Return and removes the last card of the deck
		"""
		print("Car dealt.")
		card = self.cards[-1]
		self.cards.pop()
		return card

class Player():
	"""
	Dealer class, basic hand (cards) functions, super for a human player
	"""

	def __init__(self):
		self.hand = []


	def addCard(self,card):
		""" adds a card to the player hand """
		self.hand.append(card)

	def clearHand(self):
		self.hand = []

	def showHand(self):
		""" prints the cards in the player hands"""
		for card in self.hand:
			print(card)


	def dealerFirstCard(self):
		""" prints the second of the starting 2 dealers cards"""
		print("Hidden!")
		print(self.hand[1])


	def handValue(self):
		"""
		Return the value of the players hand. Corrected for Ace value.
		"""
		total = 0
		for card in self.hand:
			total += Card.values[card.rank]

		if total > 21 and "Ace" in self.hand:
			return total - 10
		else :
			return total


class Human(Player):
	"""
	Human player, takes a pname (str) and an initial account balance (float)
	"""

	def __init__(self, pname, balance):
		self.pname = pname
		self.balance = balance
		self.hand = []

	def __repr__(self):
		return f"Name: {self.pname}\nBalance: ${self.balance}"

	def deposit(self,amount):
		""" adds an ammount (float) to the players balance"""
		self.balance += amount


	def bet(self):
		""" 
		bets (withdraw) an ammount (float) from the players balance
		returns betted amount
		"""
		while True:
			print(self)
			amount = float(input("Amount to bet: $"))
			if amount <= self.balance:
				self.balance -= amount
				return amount
				break
			else:
				print("You don't have that much money!")


def populateDeck():
	"""
	Returns a list with 52 cards (a full blackjack deck)
	"""
	suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
	ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
	cards = []
	for suit in suits:
		for rank in ranks:
			cards.append(Card(suit,rank))
	return cards

def createHumanPlayer():
	"""
	Reads a name (str) and a balance (float) and returns a new obj Human
	"""
	pname = input("Player name: ")
	balance = float(input("Starting balance: "))
	return Human(pname,balance)

def winCheck(value):
	"""
	Takes a value and returns:
	-1 if < 17 
	1 if == 21
	2 if > 21
	else 0
	"""
	if value < 17:
		return -1

	if value == 21:
		return 1

	if value > 21:
		return 2

	return 0


newgame = 'y'
player = createHumanPlayer()
dealer = Player()
status = 0	# used for storing the players hands values

while newgame.lower() != 'n':
	cls()
	deck = Deck(populateDeck())	#creates an empty deck of cards
	deck.shuffleDeck()	# shuffles the deck, clear players hands and ask for bets
	player.clearHand()	
	dealer.clearHand()
	bet = player.bet()
	print("Dealing!")
	dealer.addCard(deck.pickCard()) #pick 2 cards for each player
	dealer.addCard(deck.pickCard())
	player.addCard(deck.pickCard())
	player.addCard(deck.pickCard())

	print("\nDealer hand: ")
	dealer.dealerFirstCard()
	
	print("\nPlayer hand: ")	#print hands and values
	player.showHand()
	print(f"Hand value: {player.handValue()}")
	status = winCheck(player.handValue())
	while True:
		choice = input("Hit or stay? (H/S)\n")
		cls()
		if choice.lower() == 's':
			break
		else:
			player.addCard(deck.pickCard())
			print("\nPlayer hand: ")
			player.showHand()
			print(f"Hand value: {player.handValue()}")
			status = winCheck(player.handValue())
			if  status > 0:  #checks if 21 or busted
				break 

	if status == 1:  # if 21
		print(f"\n{player.pname} wins ${bet*2}!")
		player.deposit(bet*2)
	elif status == 2: # if busted
		print(f"\n{player.pname} is busted!")
	else: # else dealers turn
		print("\nDealers turn: ")
		print("\nDealer hand: ")
		dealer.showHand()
		print(f"Hand value: {dealer.handValue()}")
		status = -1
		while status == -1: # if < 17
			status = winCheck(dealer.handValue())
			if status == 1: # if 21
				print("\nDealer wins!")
			elif status == 2: # if busted
				print("\nDealer is busted!")
			elif status == 0: # if > 17, checks who is closest to 21
				if dealer.handValue() > player.handValue():
					print("\nDealer wins!")
				else:
					print(f"\n{player.pname} wins ${bet*2}!")
					player.deposit(bet*2)
			else:  # keeps dealing until dealer value > 17
				sleep(1)
				cls()
				dealer.addCard(deck.pickCard())
				print("\nDealer hand: ")
				dealer.showHand()
				print(f"Hand value: {dealer.handValue()}")


	newgame = input("\nPlay again? (Y/N) ")
