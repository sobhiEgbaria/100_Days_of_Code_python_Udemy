# you are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.


row1=["🤡","🤡","🤡"]
row2=["👹","👹","👹"]
row3=["🤖","🤖","🤖"]
map = [row1 ,row2,row3]

number = (input("inter number of col and row:\n"))

row = int(number[0])
col = int(number[1])




map[col-1][row-1]="x"
print(f"{row1}\n{row2}\n{row3}\n")
 