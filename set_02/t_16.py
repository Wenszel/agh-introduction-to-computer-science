from math import sqrt


def is_prime(num):
    i = 2
    while i < int(sqrt(num)) + 1:
        if num % i == 0:
            return False
        i += 1
    return True


def sum_digits(num):
    output = 0
    while num > 0:
        output += num % 10
        num //= 10
    return output


def num_divisors(num):
    output = 0
    length = 0
    div = 2
    while num > 1:
        while num % div == 0:
            output += div * (10 ** length)
            num //= div
            length += 1
        div += 1
    return output


for i in range(1, 10 ** 6):
    if not is_prime(i):
        if sum_digits(i) == sum_digits(num_divisors(i)):
            print(i)