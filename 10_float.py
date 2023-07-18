x = 3.3
y =  1.1 + 2.2
print(x)
print(y)
print(x == y)
print("*" * 15)
y_str= format(y, ".2g")
print(y_str)
y_str = float(y_str)
print(x == y_str)

print("*" * 15)
x = 3.3
y =  1.1 + 2.2
print(x)
print(y)
tolerance = 0.00001
print(abs(x - y) < tolerance)
