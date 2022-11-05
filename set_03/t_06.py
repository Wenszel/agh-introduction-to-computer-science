import random


def contains_any_odd(num):
    while num > 0:
        if num % 10 % 2 == 1:
            return True
        num //= 10
    return False


def f():
    n = int(input("n: "))
    t = [random.randrange(1, 1000) for _ in range(n)]
    print(t)
    for el in t:
        if not contains_any_odd(el):
            return False
    return True


print(f())
