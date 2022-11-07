from random import randint
N = int(input("Array length: "))
M = N * N
t1 = [sorted([randint(1, 10) for _ in range(N)]) for _ in range(N)]
t2 = [0 for _ in range(M)]
print("Array 1:\n", t1)
for i in range(N):
    index = 0
    for j in range(N):
        while t2[index] != 0 and t2[index] < t1[i][j]:
            index += 1
        if t2[index] != t1[i][j]:
            for k in range(M - 1, index, -1):
                t2[k] = t2[k - 1]
            t2[index] = t1[i][j]
print("Array 2\n", t2)

