# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.

love_counter = 0
true_counter = 0
first_name = input("inter the first name:\n")
second_name = input("inter the second name:\n")

both_names = (first_name + second_name).lower()

love_counter += both_names.count("l")
love_counter += both_names.count("o")
love_counter += both_names.count("v")
love_counter += both_names.count("e")

true_counter += both_names.count("t")
true_counter += both_names.count("r")
true_counter += both_names.count("u")
true_counter += both_names.count("e")

final_sum = (true_counter * 10) + love_counter

if final_sum <= 10 or final_sum >= 90:
    print(f"Your score is {final_sum}, you go together like coke and mentos.")
elif final_sum >= 40 and final_sum <= 50:
    print(f"Your score is {final_sum}, you are alright together.")
else:
    print(f"Your score is {final_sum}")
