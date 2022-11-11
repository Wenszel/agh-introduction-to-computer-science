from random import randint


def is_complex(num):
    if num <= 2:
        return False
    i = 2
    while i * i < num:
        if num % i == 0:
            return True
        i+=1
    return False


def f():
    n = int(input("n: "))
    t = [[[randint(1, 10 ** 2) for _ in range(n)] for _ in range(n)] for _ in range(n)]
    neighborhood = [(-1, -1),(-1,0),(-1,1),
                 (0, -1), (0, 1), (-1, 1), (1, 0),(1, 1)]
    for level in range(n):
        quantity = 0
        for y in range(1, n - 1):
            for x in range(1, n - 1):
                for neighbor in neighborhood:
                    if is_complex(t[level][y + neighbor[0]][x+ neighbor[1]]):
                        quantity += 1
        if quantity == 0:
            return False
    return True


print(f())
