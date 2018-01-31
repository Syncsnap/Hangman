from random import randint
import hangclass

def wordLook():
	"""Open random word file and pick word"""
	f = open('hangwords.txt', 'r')
	wordChoice = f.readlines()
	word = wordChoice[randint(0, 853)]
	# break up word into list format tp serperate the letters 
	wordList = list(word.lower())
	# Delete the \n at end of string
	wordList.pop()
	f.close()
	return wordList
	

toGuess = wordLook()
output = ['_'] * len(toGuess)
player = hangclass.player()
# turn list into readable string
strings = ''.join(toGuess)

print "\n----------------------------------------------------------------------"
print "Welcome to hangman! You have 10 tries to guess the secret word, else you die!"
print "----------------------------------------------------------------------\n\n"


def checkLetter():
	""" Function checks if input is correct, one letter only!"""
	guess = False
	while guess != True:
		guess = str(raw_input("Guess a letter: "))
		if guess.isalpha() and len(guess) == 1 :
			return guess
		elif not guess.isalpha() or len(guess) > 1:
			print "The input may be one letter only!"
		else:
			print "Error in checkLetter"

def hangMan():
	# Main environment, checks if letter in word
	guess = checkLetter()
	guessedLetters = player.guessedLetters
	correctLetters = player.correctLetters

	# Check if letter is already guessed before
	if guess in player.guessedLetters or guess in correctLetters:
		print "You have already tried that letter!\n"
		hangMan()
	# If guess in word and not guessed yet, print in right position
	elif guess in toGuess:
		for i,x in enumerate(toGuess):
			if x is guess:
				player.correctLetters.append(guess)
				output[i] = guess
		# If all letters guessed: Win condition and try again prompt
		# Letters are sorted alphabetically!
		if sorted(correctLetters) == sorted(toGuess):
			print "The word is: %s\n" % strings
			print "You won! \n"
			tryAgain()
		print_output()
		hangMan()
	#If wrong letter, subtract amount of tries 
	elif guess not in player.guessedLetters and guess not in toGuess:
		player.wrongGuess()
		print "\nThat letter isn't in the word!\n"
		player.guessedLetters.append(guess)
		print "These are your guessed letters: "
		print player.guessedLetters
		print "\n You have ", player.triesLeft, "tries left"
		print "-----------------------\n"
		print "\n"
		loseGame()
	else:
		print "Error in hangMan()"

def print_output():
	""" print letters in correct places as string"""
	print ''.join([str(x)+"" for x in output])

def loseGame():
	""" Check how many tries left -> If zero print correct word and try again prompt"""
	if player.triesLeft == 0:
		print "You lose! the word was: %s" % strings
		tryAgain()
	elif player.triesLeft > 0:
		hangMan()
	else:
		print "Error in loseGame()"

def tryAgain():
	""" Reset game state and start over or quit game""" 
	global toGuess
	global output
	tryAgain = raw_input("Try again? y/n\n")
	if tryAgain == "y" or tryAgain == "Y":
		toGuess = wordLook()
		player.guessedLetters = []
		player.correctLetters = []
		player.triesLeft = 10
		output = ['_'] * len(toGuess)
		hangMan()
	elif tryAgain == "n" or tryAgain == "N":
		print "That's a shame! See you next time :)"
		quit()
	else:
		print "Input not accepted..."
		tryAgain()

hangMan()

