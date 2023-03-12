from math import sqrt


def get_prime_divs(num: int) -> list:
    output = set()
    div = 2
    while div <= sqrt(num):
        if num % div == 0:
            output.add(div)
        else:
            div += 1
    if num>1:
        output.add(num)
    return list(output)


def f(t, i=0):
    print(i)
    if i == len(t) - 1:
        return True
    ks = get_prime_divs(t[i])
    print(ks)
    if len(ks) == 0:
        return False
    for k in ks:
        f(t, i+k)


print(f([32, 231, 32, 231, 3, 2, 321, 12, 21, 21, 21, 11, 11, 42, 45]))
