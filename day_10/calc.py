import logo
import os

clear = lambda: os.system("cls")
print(logo.logo)


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("what is the first number?: "))
num2 = int(input("what is the second number?: "))

for i in operation:
    print(i)

operation_symbol = input("pick an operation symbol?: ")

fun = operation[operation_symbol]

res = fun(num1, num2)

print(f"{num2} {operation_symbol} {num2} = {res}")
