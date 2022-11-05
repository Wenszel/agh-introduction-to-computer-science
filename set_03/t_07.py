import random


def contains_only_odd(num) -> bool:
    while num > 0:
        if num % 10 % 2 == 0:
            return False
        num //= 10
    return True


def f():
    n = int(input("n: "))
    t = [random.randrange(1, 1000) for _ in range(n)]
    for el in t:
        print(el, contains_only_odd(el))


f()
