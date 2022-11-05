from random import randrange
n = int(input(""))
t = [randrange(100, 999) for _ in range(n)]
max_length = 1
print(t)
for i in range(0, n):
    for j in range(n - 1, i, -1):
        if t[i] == t[j]:
            length = 1
            while t[i + length] == t[j - length]:
                length += 1
            if max_length < length:
                max_length = length

print(max_length)
