# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
import random

names = input(
    "inter all the names: the name must have , and space like [Sobhi, Egbaria]\n"
)

list_of_names = names.split(", ")

number_of_names = len(list_of_names)

random_num = random.randint(0, (number_of_names - 1))

print(f"{list_of_names[random_num]} your turn to pay ")
