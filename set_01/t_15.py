from math import sqrt
eps = 10 ** -10
x = sqrt(0.5)
a = 1
b = 0.5
while abs((2 / a) - (2 / b)) > eps:
    b = a
    a *= x
    x = sqrt(0.5 + (0.5 * x))
print(2 / a)
