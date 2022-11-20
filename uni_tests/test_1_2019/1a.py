from math import sqrt
from random import randint


def is_power(number):
    b = 2
    while b <= int(sqrt(number)):
        p = 2
        while b ** p < number:
            p += 1
        if b ** p == number:
            return True
        b += 1
    return False


def f(t1, t2):
    for l1 in range(1, 24):
        l2 = 24 - l1
        for i in range(0, len(t1) - l1):
            for j in range(0, len(t2) - l2):
                total = 0
                for k in range(l1):
                    total += t1[i + k]
                for k in range(l2):
                    total += t2[j + k]
                if is_power(total):
                    return True
    return False


print(f([randint(1, 10 ** 3) for _ in range(20)], [randint(1, 10 ** 3) for _ in range(20)]))

