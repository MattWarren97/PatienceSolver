from PatienceGame import PatienceGame


def getPremadeBoard():
	cards = [	"..", "s3", "s4", "hA", "h7", "c7", "d4", "s6",
				"..", "h6", "s7", "c6", "d6", "h5", "sA", "d2",
				"..", "c3", "d3", "h4", "s2", "s5", "cA", "h3",
				"..", "c5", "c4", "d7", "c2", "h2", "dA", "d5"]
	return cards

def main():
	possibleVictoryCount = 0
	gameCount = 100
	gameAttemptCount = 10000
	for i in range(gameCount):
		game = PatienceGame(7)
		for j in range(gameAttemptCount):

			victory = game.winGame()
			if victory:
				possibleVictoryCount += 1
				break
			else:
				game.resetBoard()

	print("\nSuccesful " + str(possibleVictoryCount) + " out of " + str(gameCount) + " times!")
	#game = PatienceGame()

if __name__ == "__main__":
	main()
