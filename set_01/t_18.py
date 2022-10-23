eps = 1e-10
n = int(input())
a, h = n, 1 / n
while abs(a - h) > eps:
    a = (a+h) / 2
    h = n / (a*a)
print((a + a + h) / 3)
