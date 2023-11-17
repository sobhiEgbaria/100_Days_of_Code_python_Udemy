import logo
import random

print(logo.logo)
print("Welcome to the number guessing game")
print(f"I'm thinking of a number between [1 - 100]")
difficulty = input("Choose a difficulty: Type 'Easy' or 'Hard': ").lower()
correct_number = random.randint(1, 100)
keep_playing = True
attempts = 10
if difficulty == "hard":
    attempts = 5


while keep_playing:
    print(f"You have a {attempts} remaining to guess the number: {correct_number} ")
    guess = int(input("Make a guess: "))
    attempts -= 1
    if attempts == 0:
        print(f"You've run out of guesses, You Lost!!!!!")
        break
    elif guess == correct_number:
        print(f"You got it! the answer was {guess}")
        break
    elif guess > correct_number:
        print(f"Too Hight!!!")
    elif guess < correct_number:
        print(f"Too Low!!!")
