import random
import time

word_list = ["planete", "dinosaure", "lune", "soleil", "pokemon"]
prop = []
word = random.choice(word_list)
word_tf = ("-") * len(word)
wrong = 0
max_mistake = len(word) - 1

print("The word you need to find:")
print(word_tf)

while word_tf != word and wrong < max_mistake:

	print("\nWord to find: ", word_tf)
	print("Letter already used: ", prop)
	print("\nNumber of try left: ", (max_mistake - wrong))


	guess = input("Guess a letter: ").lower()

	while guess in prop:
		print ("You already used this letter.\n")
		guess = input("Guess a letter: ").lower()
	prop.append(guess)

	if len(guess) > 1:
		print("\nPlease enter only one character!\n")
		prop.remove(guess)

	elif guess.isalpha() == False:
		print("\nPlease enter only a letter\n")
		prop.remove(guess)

	elif guess in word:

		new = ""

		for i in range(len(word)):
			if guess == word[i]:
				new += guess
			else:
				new += word_tf[i]
		word_tf = new

	else:
		print("\nIncorrect! Try again!\n")
		wrong += 1

if wrong == max_mistake:
	print("Sorry you don't have any try left. Better luck next time.")

else:
	print("Congrats! You found the right word !\nIt was: ",word)