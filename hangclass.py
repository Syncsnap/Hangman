class player:
	def __init__(self):
		self.triesLeft = 10
		self.guessedLetters = []
		self.correctLetters = []
	def wrongGuess(self):
		self.triesLeft = self.triesLeft - 1
