from random import randint


def f(t):
    for y in range(len(t)):
        for x in range(len(t)):
            flag = False
            if t[y][x] == 0:
                flag = True
            if not flag:
                return flag
    for x in range(len(t)):
        for y in range(len(t)):
            flag = False
            if t[y][x] == 0:
                flag = True
            if not flag:
                return flag
    return True


n = int(input("n: "))
array = [[randint(-100, 100) for _ in range(n)] for _ in range(n)]
print(f(array))