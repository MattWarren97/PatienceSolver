
class Card:
	def __init__(self, suit, number):
		self.suits = ["\u2665", "\u2663", "\u2666", "\u2660"] #Hea, Cl, Dia, Sp
		self.nums = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

		self.suit = suit
		self.number = number

	def getString(self):
		return self.getSuitStr() + self.getNumStr()

	def getSuitStr(self):
		return self.suits[self.suit]

	def getNumStr(self):
		return self.nums[self.number]

	def getNumber(self):
		return self.number

	def __repr__(self):
		return self.getString()


		

