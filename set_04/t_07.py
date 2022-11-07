from random import randint
N = int(input("Array length: "))
M = N * N
t1 = [sorted([randint(1, 10 ** 2) for _ in range(N)]) for _ in range(N)]
t2 = [0 for _ in range(M)]
print("Array 1:\n", t1)
for i in range(N):
    index = M - 1
    for j in range(N-1, -1, -1):
        while t2[index] >= t1[i][j]:
            index -= 1
        for k in range(index):
            t2[k] = t2[k + 1]
        t2[index] = t1[i][j]
        print(t2)
print("Array 2\n", t2)

