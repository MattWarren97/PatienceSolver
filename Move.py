from Card import Card

class Move:
	def __init__(self, card, newPos, oldPos):
		self.card = card
		self.newPos = newPos
		self.oldPos = oldPos

	def getPosStr(self, pos):
		return "(" + str(pos[0]) + "," + str(pos[1]) + ")"

	def __repr__(self):
		toPrint = ""
		toPrint += "Move: " + str(self.card)
		toPrint += " from " + self.getPosStr(self.oldPos)
		toPrint += " to " + self.getPosStr(self.newPos)
		toPrint += "\n"
		
		return toPrint

	def getOldPos(self):
		return self.oldPos

	def getNewPos(self):
		return self.newPos

	def getCard(self):
		return self.card

	