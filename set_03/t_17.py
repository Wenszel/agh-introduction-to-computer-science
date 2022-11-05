from random import randint
from math import sqrt


def dec_to_bin(num) -> int:
    output = 0
    power = 0
    while num > 0:
        output += (num % 2) * (10 ** power)
        num //= 2
        power += 1
    return output


def is_prime(num) -> bool:
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            return False
    return True


def generate_sum(t1, t2, length, mask) -> int:
    output = 0
    for i in range(length):
        if mask % 2 == 0:
            output += t1[i]
        else:
            output += t1[i] + t2[i]
        mask //= 10
    return output


def f():
    n = int(input("n: "))
    t1 = [randint(1, 10 ** 5) for _ in range(n)]
    t2 = [randint(1, 10 ** 5) for _ in range(n)]
    for i in range(2 ** n):
        generated_sum = generate_sum(t1, t2, n, dec_to_bin(i))
        if is_prime(generated_sum):
            print(generated_sum)


f()


