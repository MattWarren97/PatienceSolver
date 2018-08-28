from PatienceGame import PatienceGame


def getPremadeBoard():
	cards = [	"..", "s2", "s4", "hA", "h7", "c7", "d4", "s6",
				"..", "h6", "s7", "c6", "d6", "h5", "sA", "h2",
				"..", "s3", "d3", "h4", "s2", "s5", "cA", "h2",
				"..", "s5", "s4", "d7", "s2", "h2", "dA", "d5"]
	return cards

def main():
	victoryCount = 0
	gameCount = 100
	for i in range(gameCount):
		game = PatienceGame(7, getPremadeBoard())
		victory = game.winGame()
		if victory:
			victoryCount += 1

	print("We won " + str(victoryCount) + " out of " + str(gameCount) + " times!")
	#game = PatienceGame()

if __name__ == "__main__":
	main()
