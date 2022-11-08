from random import randint


def digits(number):
    d = [False for _ in range(10)]
    while number > 0:
        d[number % 10] = True
        number //= 10
    return d


def is_friendly(n1, n2):
    d1 = digits(n1)
    d2 = digits(n2)
    for i in range(0, 9):
        if d1[i] != d2[i]:
            return False
    return True


def f(t):
    output = 0
    for y in range(len(t)):
        for x in range(len(t)):
            flag = True
            if 0 < x + 1 < len(t):
                if not is_friendly(t[x][y], t[y][x + 1]):
                    flag = False
            if flag and 0 < x - 1 < len(t):
                if not is_friendly(t[x][y], t[y][x - 1]):
                    flag = False
            if flag and 0 < y - 1 < len(t):
                if not is_friendly(t[x][y], t[y - 1][x]):
                    flag = False
            if flag and 0 < y + 1 < len(t):
                if not is_friendly(t[x][y], t[y + 1][x]):
                    flag = False
            if flag:
                output += 1
    return output


n = int(input("n: "))
array = [[randint(-100, 100) for _ in range(n)] for _ in range(n)]
print(f(array))
