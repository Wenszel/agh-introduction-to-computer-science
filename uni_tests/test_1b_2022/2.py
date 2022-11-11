def square(t):
    for i in range(1, len(t)):
        for y in range(0, len(t) - i):
            for x in range(0, len(t) - i):
                p = t[y][x] * t[y][x+i] * t[y+i][x] * t[y+i][x+i]
                if has_two_factors(p):
                    return i + 1
    return 0


def has_two_factors(n):
    amount = 0
    i = 2
    while n > 1:
        if n % i == 0:
            while n % i == 0:
                n /= i
            amount += 1
        i += 1
    return amount == 2
