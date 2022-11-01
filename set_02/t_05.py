def to_bin(n, p=1):
    if n == 0:
        return 0
    return n % 2 * p + to_bin(n // 2, p * 10)


def int_len(n):
    length = 0
    while n > 0:
        n //= 10
        length += 1
    return length


def is_divisible(n, d, mask):
    output = 0
    length = int_len(n)
    p = 1
    for _ in range(length):
        if mask % 10 == 1:
            output += (n % 10) * p
            p *= 10
        mask //= 10
        n //= 10
    return output % d == 0


num = int(input('num: '))
div = int(input('div: '))

result = 0
for i in range(1, 2 ** int_len(num)):
    if is_divisible(num, div, to_bin(i)):
        result += 1

print(result)
