result = 0

for number in range(1, 101):
    if number % 2 == 0:
        result += number

print(f"{result}")
