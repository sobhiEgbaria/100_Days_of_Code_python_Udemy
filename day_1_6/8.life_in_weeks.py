days_in_year = 365
weeks_in_year = 52
months_in_year = 12

age = int(input("inter your age:"))
max_age = 90
days_left = (max_age - age) * 365
weeks_left = (max_age - age) * 52
months_left = (max_age - age) * 12

print(
    f"if you lucky to live 90 years you have a {days_left} day {weeks_left} weeks and {months_left} months"
)
