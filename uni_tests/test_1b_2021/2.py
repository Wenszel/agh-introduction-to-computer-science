from math import floor, log10


def f(N):
    num_len = floor(log10(N)) + 1
    output = None
    for i in range(0, num_len):
        N = (N // 10) + ((N % 10) * (10 ** (num_len - 1)))
        for b in range(2, 16 + 1):
            if is_task_condition(N, b):
                if output is None or output > b:
                    output = b
                break
    print(output)


def is_task_condition(n, sys):
    product = 1
    while n > 0:
        product *= n % sys
        n //= sys
    if product <= 1:
        return False
    i = 2
    while i * i < product:
        if product % i == 0:
            return False
        i += 1
    return True


f(1428)