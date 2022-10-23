from math import sqrt
a = int(input("Enter a"))
b = int(input("Enter b"))
e = 1e-6
while abs(a - b) > e:
    a, b = sqrt(a * b), (a + b) / 2
print((a + b) / 2)
