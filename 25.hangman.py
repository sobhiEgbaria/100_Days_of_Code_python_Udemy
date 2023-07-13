import random

word_list = ["aardvark", "baboon", "camel"]

# -1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# -2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# -3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = random.choice(word_list)
users_guess = input("enter your guess:\n")
print(chosen_word)

for chr in range(len(chosen_word)):
    if users_guess == chosen_word[chr]:
        print("right")
    else:
        print("wrong")
