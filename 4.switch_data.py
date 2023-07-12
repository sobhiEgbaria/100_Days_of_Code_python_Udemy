a = input("num A is:")
b = input("num B is:")

print(f"before switching A={a} b={b}")

a, b = b, a
print(f"after switching A={a} b={b}")
