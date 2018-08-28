from Card import Card
from random import shuffle
from Move import Move
import time

#board is a numSuits x numCards list 
#boardPositions are specified as Col x Row, board position board[row][col] is (col, row)

class PatienceGame:
	def __init__(self):
		self.numCards = 7
		self.numSuits = 4
		self.cards = []
		self.OOPaces = []
		self.board = []
		self.spaces = []
		self.followingCards = {}
			
		for row in range(self.numSuits):
			self.board.append([])
			self.spaces.append((0, row))
		
		self.createCards()
		self.dealBoard()

		#self.getMoves()

		#self.winGame()

	def winGame(self):
		moves = self.getMoves()
		while len(moves) != 0:
			moves = self.getMoves()
			#print("Length of moves is " + str(len(moves)))
			if (len(moves) == 0):
				print("GAME OVER")
				victory = self.isGameWon()
				if victory:
					print("\n GAME WON!! Congratulations.")
				else:
					print("\n GAME LOST. Commiserations.")
				self.printBoard()
				return victory
			#print("Next move is " + str(moves[0]))

			#time.sleep(5)
			self.makeMove(moves[0])
		
	def isGameWon(self):
		for row in range(self.numSuits):
			prevCard = self.board[row][0]

			for col in range(1, self.numCards+1):
				newCard = self.board[row][col]
				if not (newCard is self.getFollowingCard(prevCard)):
					toPrint = ""
					toPrint += "Failed, as prevCard: " + str(prevCard)
					toPrint += " expected " + str(self.getFollowingCard(prevCard))
					toPrint += " not " + str(newCard)
					print(toPrint)
					return False
				prevCard = newCard
		print("Game completion check complete, no failures")
		return True	

	def createCards(self):
		for s in range(self.numSuits):
			prevCard = None
			for n in range(self.numCards):
				c = Card(s, n)
				self.cards.append(c)
				if n == 0: #card is an ace
					self.OOPaces.append(c)
				else: #card will be following a different card
					self.followingCards[prevCard] = c
				prevCard = c



	def dealBoard(self):
		shuffle(self.cards)
		for row in range(self.numSuits):
			self.board[row].append(None)
			for col in range(1, self.numCards+1):
				c = self.cards[row*self.numCards + (col-1)]
				self.board[row].append(c)

		print("Initial Board:\n")
		self.printBoard()


	def printBoard(self):
		toPrint = ""
		for row in range(self.numSuits):
			for col in range(self.numCards+1):
				c = self.board[row][col]
				if c is None:
					toPrint += "..." + "\t"
				else:
					toPrint += str(c) + "\t"
			toPrint += "\n"
		print(toPrint)


	def getMoves(self):
		moves = []
		for s in self.spaces:
			(col, row) = s
			if col == 0:
				for a in self.OOPaces:
					m = Move(a, s, self.findCard(a))
					moves.append(m)
			else:
				prevCard = self.board[row][col-1]
				if not (prevCard is None):
					folCard = self.getFollowingCard(prevCard)
					if not (folCard is None):
						m = Move(folCard, s, self.findCard(folCard))
						moves.append(m)
		shuffle(moves)
		return moves

	def getFollowingCard(self, prevCard):
		if prevCard.getNumber() == (self.numCards-1):
			#print(str(prevCard) + " has no following card.\n")
			return None
		folCard = self.followingCards[prevCard]
		#print("folCard of " + str(prevCard) + " is " + str(folCard))
		return folCard

	def findCard(self, card):
		for row in range(self.numSuits):
			for col in range(self.numCards+1):
				if self.board[row][col] is card:
					return (col, row)

		#else
		print("ERROR: failed to find card: ", card, ". Board is: \n")
		self.printBoard()
		return None


	def makeMove(self, move):
		op = move.getOldPos()
		np = move.getNewPos()
		c = move.getCard()


		self.board[op[1]][op[0]] = None
		self.board[np[1]][np[0]] = c

		if c in self.OOPaces:
			self.OOPaces.remove(c)
			#print("Removed one OOP ace")

		self.spaces.remove(np)
		self.spaces.append(op)
		#self.printBoard()

