n = int(input())
i = 10
while i > n % 10:
    i = n % 10
    n //= 10
print(n == 0)
