# This is how you work out whether if a particular year is a leap year.
##### on every year that is evenly divisible by 4
##### **except** every year that is evenly divisible by 100
#### **unless** the year is also evenly divisible by 400

year = int(input("inter a year:\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("the year is leap")
        else:
            print("the year is not leap")
    else:
        print("the year is not leap")
else:
    print("the year is not leap.")
