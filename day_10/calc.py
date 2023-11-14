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

"""
the full solution
"""

# def calculator():
#     keep_on = True

#     num1 = float(input("what is the first number?: "))
#     for i in operation:
#         print(i)
#     operation_symbol = input("pick an operation symbol?: ")
#     num2 = float(input("what is the second number?: "))

#     operation_function = operation[operation_symbol]

#     res = operation_function(num1, num2)

#     print(f"{num1} {operation_symbol} {num2} = {res}")

#     while keep_on:
#         keep_on = input(
#             f"type 'Y' to continue calculate with {res}, or 'N' to start new calculation: "
#         ).lower()
#         if keep_on == "n":
#             clear()
#             calculator()
#         else:
#             operation_symbol = input("pick an operation symbol?: ")
#             num3 = int(input("what is the new number??: "))
#             num2 = res
#             operation_function = operation[operation_symbol]
#             res = operation_function(res, num3)
#             print(f"{num2} {operation_symbol} {num3} = {res}")


# calculator()

# ## ========================================================================================
# """
# anther solution (shorter)
# """


# def calculator():
#     keep_on = True

#     num1 = float(input("what is the first number?: "))
#     for i in operation:
#         print(i)
#     operation_symbol = input("pick an operation symbol?: ")

#     while keep_on:
#         num2 = float(input("what is the anther number?: "))
#         operation_function = operation[operation_symbol]
#         res = operation_function(num1, num2)

#         print(f"{num1} {operation_symbol} {num2} = {res}")

#         keep_on = input(
#             f"type 'Y' to continue calculate with {res}, or 'N' to start new calculation: "
#         ).lower()
#         if keep_on == "n":
#             clear()
#             calculator()
#         else:
#             operation_symbol = input("pick an operation symbol?: ")
#             num1 = res


# calculator()
