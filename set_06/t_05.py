def f(T, start=0, end=1):
    if end - start > 30:
        return False
    if end >= len(T) - 1:
        if start == 0:
            return False
        return is_prime(T[start: end + 1])
    if is_prime(T[start:end + 1]):
        return f(T, start, end + 1) or f(T, end + 1, end + 2)
    return f(T, start, end + 1)


def is_prime(n: list) -> bool:
    output = 0
    power = 0
    for i in reversed(n):
        output += i * (2 ** power)
        power += 1
    if output == 1 or output == 0:
        return False
    i = 2
    while i * i <= output:
        if output % i == 0:
            return False
        i += 1
    return True


test1 = [1, 1, 1, 0, 1, 1]
test2 = [1, 1, 0, 1, 0, 0]
print(f(test1))
print(f(test2))