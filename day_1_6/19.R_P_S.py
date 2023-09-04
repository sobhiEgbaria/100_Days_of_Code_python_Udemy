import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\n"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
\n"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
\n"""


list_of_choices = [rock, paper, scissors]

computer_choice = random.randint(1, 3)
player_choice = int(input("type 1 for rock, 2 for paper 3 for scissors:\n"))

if player_choice > 3:
    print("you inset an invalid number = you lost")
else:
    print(
        f"your choice:\n{list_of_choices[player_choice-1]}\n computer choice\n{list_of_choices[computer_choice-1]}"
    )

    if player_choice == computer_choice:
        print("Draw")
    elif player_choice == 1 and computer_choice == 2:
        print("you lost")
    elif player_choice == 1 and computer_choice == 3:
        print("you won")
    elif player_choice == 2 and computer_choice == 1:
        print("you won")
    elif player_choice == 2 and computer_choice == 3:
        print("you lost")
