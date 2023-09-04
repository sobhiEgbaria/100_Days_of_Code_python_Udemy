import random
import logo
import hangman_words


print(logo.logo)
spaces = []
remain_guess = 0
lives = 6

chosen_word = random.choice(hangman_words.word_list)
remain_guess = len(chosen_word)

for i in range(len(chosen_word)):
    spaces.append("_")

while remain_guess > 0 and lives > 0:
    print(spaces)
    users_guess = input("enter your guess:\n")
    if users_guess not in chosen_word:
        print(logo.stages[lives])
        lives -= 1
    for chr in range(len(chosen_word)):
        if users_guess == chosen_word[chr]:
            spaces[chr] = chosen_word[chr]
            remain_guess -= 1

if remain_guess > lives:
    print(f"{logo.stages[0]}\nyou lost")
else:
    print("you won")
