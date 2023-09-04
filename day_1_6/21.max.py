all_scores = input("all the plyer scores:\n").split(" ")
max = 0
for i in all_scores:
    temp = int(i)
    if temp > max:
        max = temp

print(f"the max score is: {max}")
