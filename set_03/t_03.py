from math import ceil, sqrt


def f(n):
    t = [True for _ in range(n)]
    t[0], t[1] = False, False
    for i in range(2 * ceil(sqrt(n))):
        if t[i]:
            for j in range(i*i, n, i):
                t[j] = False
    for k in range(0, n):
        if t[k]:
            print(k)


num = int(input())
f(num)
