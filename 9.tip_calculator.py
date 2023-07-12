print("welcome to the tip calculator: ")

total_bill = float(input("what was the total?"))
tip = int(input("what percentage of tip would like to give? 10 12 or 15 "))
num_of_people = int(input("how many people will split the pill? "))

percentage_of_tip = tip / 100
bill_with_tip = total_bill + (total_bill * percentage_of_tip)

one_person_payment = round((bill_with_tip / num_of_people), 2)
print(f"each one have to pay ${one_person_payment}")
