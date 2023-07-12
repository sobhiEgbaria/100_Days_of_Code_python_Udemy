# Password Generator Project

# Easy Level - Order not randomized:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Hard Level - Order of characters randomized:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

Total_char = nr_letters + nr_symbols + nr_numbers
password = []
password1 = ""

for i in range(0, Total_char):
    if nr_letters > 0:
        password.append(random.choice(letters))
        nr_letters -= 1
    elif nr_symbols > 0:
        password.append(random.choice(symbols))
        nr_symbols -= 1

    elif nr_numbers > 0:
        password.append(random.choice(numbers))
        nr_numbers -= 1
random.shuffle(password)

for char in password:
    password1 += char


print(password1)
