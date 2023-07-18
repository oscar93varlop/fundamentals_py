print(not True)
print(not False)

print("NOT AND")
print("NOT (True And True) =>", not (True and True))
print("NOT (True And False) =>", not (True and False))
print("NOT (False And True) =>", not (False and True))
print("NOT (False And False) =>", not (False and False))

stock = int(input("ingresa la cantidad de su stock"))
print(not (stock >= 100 and stock <= 1000))