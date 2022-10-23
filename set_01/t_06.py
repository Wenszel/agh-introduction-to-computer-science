eps = 1e-10
a = 0
b = 100
while (b - a) > eps:
    c = 0.5 * (a + b)
    if c**c - 2022 < 0:
        a = c
    else:
        b = c
print(a)
