from math import sqrt


def sum_divisors(num):
    output = 1
    for div in range(2, int(sqrt(num)+1)):
        if num % div == 0:
            output += div
            output += num // div
    return output


for i in range(1, 10 ** 6):
    i_divisors = sum_divisors(i)
    j_divisors = sum_divisors(i_divisors)
    if i == j_divisors and i_divisors > i:
        print(i, i_divisors)

