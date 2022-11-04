n = int(input("n: "))
t = [0 for _ in range(10)]
while n != 0:
    n = int(input("n: "))
    if t[0] < n:
        i = 0
        while t[i] < n and i <= 8:
            t[i] = t[i + 1]
            i += 1
        t[i] = n
print(t[0])

