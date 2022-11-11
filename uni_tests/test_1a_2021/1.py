from math import floor, log10


def f(K: int) -> int:
    length = floor(log10(K)) + 1
    max_num = 0
    for M in range(0, length):
        num = K % (10 ** (length - M))
        for N in range(0, length - M):
            num //= 10
            if is_prime(num) and max_num < num:
                max_num = num
    return max_num


def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i < n:
        if n % i == 0:
            return False
        i += 1
    return True


print(f(1202742516))