from math import floor, log10


def print_prime(n: int, mask=1):
    if mask < 2 ** (floor(log10(n)) + 1) - 1:
        num = cut(n, to_bin(mask))
        if is_prime(num):
            print(num)
        return print_prime(n, mask + 1)


def cut(n: int, m: int) -> int:
    output = 0
    power = 0
    while m > 0:
        if m % 10 == 1:
            output += (n % 10) * (m % 10) * (10 ** power)
            power += 1
        n //= 10
        m //= 10
    return output


def to_bin(num):
    output = 0
    power = 0
    while num > 0:
        output += (num % 2) * (10 ** power)
        power += 1
        num //= 2
    return output


def is_prime(n: int) -> bool:
    if n == 1:
        return False
    i = 2
    while i * i < n:
        if n % i == 0:
            return False
        i += 1
    return True


print_prime(2137)
