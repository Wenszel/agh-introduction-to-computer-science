from math import log10


def f(n, c=0, i=1, flag=False):
    length = int(log10(n)) + 1
    if is_prime(c) and c > 9 and flag and c != n:
        print(c)
    if length == i:
        return
    new_n = 10 * c + n // 10 ** (length - i) % 10
    return f(n, new_n, i+1, True) or f(n, c, i+1)


def is_prime(n: int) -> bool:
    if n == 1:
        return False
    i = 2
    while i * i < n:
        if n % i == 0:
            return False
        i += 1
    return True


f(1234)
