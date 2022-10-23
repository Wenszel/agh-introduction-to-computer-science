x = int(input())
fact = 1
total = 0
a = 1
n = 0
while abs(a) < 10 ** (-6):
    if n > 0:
        fact *= (2*n) - 1
        fact *= 2 * n
    a = ((-1) ** n) * (x**(2*n))
    a /= fact
    total += a
    n += 1
print(total)
