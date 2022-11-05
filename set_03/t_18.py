from random import randint
n = int(input("n: "))
t = [randint(1, 10 ** 5) for _ in range(n)]
max_length = 0
for i in range(n):
    for j in range(n - 1, i, -1):
        length = 0
        if t[i + length] % 2 == 1:
            while t[i + length] == t[j - length]:
                    length += 1
                    if max_length < length:
                        max_length = length
print(max_length)