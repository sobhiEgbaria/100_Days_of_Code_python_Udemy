# You are going to write a program that calculates the average student height from a List of heights.

student_heights = input("enter students height:\n").split(" ")
sum_of_height = 0
counter = 0

for i in student_heights:
    sum_of_height += int(i)
    counter += 1

avg = sum_of_height / counter

print(round(avg))
