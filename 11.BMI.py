# BMI using IF AND elif
weight = float(input("inter your weight in kg:\n"))
height = float(input("inter your height in m:\n"))

bmi = round(weight / height**2)

if bmi < 18.5:
    print(f"your BMI is: {bmi}, and you have underweight")
elif bmi < 25:
    print(f"your BMI is: {bmi}, you have a normal weight ")
elif bmi < 30:
    print(f"your BMI is: {bmi}, you have slightly overweight")
elif bmi < 35:
    print(f"your BMI is: {bmi}, you have obese")
else:
    print(f"your BMI is: {bmi}, you have clinically obese")
