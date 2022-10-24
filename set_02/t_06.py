from math import sqrt
n = int(input())
i = int(sqrt(n))
while n % i != 0:
    i -= 1
print(i, n // i)
