a = int(input("Enter first number"))
b = int(input("Enter second number"))
eps = 1e-10
while abs(a/b - b/(a+b)) > eps:
    a, b = b, a+b
print(a/b)
