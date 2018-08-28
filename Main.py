from PatienceGame import PatienceGame

def main():
	victoryCount = 0
	gameCount = 10000
	for i in range(gameCount):
		game = PatienceGame()
		victory = game.winGame()
		if victory:
			victoryCount += 1

	print("We won " + str(victoryCount) + " out of " + str(gameCount) + " times!")
	#game = PatienceGame()

if __name__ == "__main__":
	main()