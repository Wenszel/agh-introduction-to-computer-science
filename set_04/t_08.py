from random import randint
N = int(input("Array length: "))
M = N * N
t = [[randint(1, 10 ** 2) for _ in range(N)] for _ in range(N)]
max_length = 0
for i in t:
    for j in i:
        print(j, end=" ")
    print("")

for y in range(N - 1):
    for x in range(N - 1):
        i = 1
        length = 2
        q = t[y][x] / t[y + 1][x + 1]
        while x + i < N and y + i < N and t[y][x] / t[y+i][x+i] == q ** i:
            i += 1
            length += 1
        if max_length < length:
            max_length = length
print(max_length)