# build an automatic pizza order program.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

final_praise = 0

pizza_size = input("what size pizza do you want? S, M or L.\n")
if pizza_size == "s":
    final_praise += 15
elif pizza_size == "m":
    final_praise += 20
elif pizza_size == "l":
    final_praise += 25
Pepperoni = input("do you want Pepperoni? y or n.\n")
if Pepperoni == "y":
    if pizza_size == "s":
        final_praise += 2
    else:
        final_praise += 3
Extra_cheese = input("do you want Extra cheese? y or n.\n")
if Extra_cheese == "y":
    final_praise += 1

print(f"your final bill is {final_praise}")
