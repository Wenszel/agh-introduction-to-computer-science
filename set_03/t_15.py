from random import randint
import math
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def f():
    t = [randint(1, 10 ** 5) for _ in range(10 ** 6)]
    a = b = 1
    any_prime = False
    for i in range(10 ** 4):
        if i == a:
            if is_prime(t[a]):
                return False
            a, b = b, a + b
        else:
            if is_prime(t[i]):
                any_prime = True
    return True and any_prime


print(f())


