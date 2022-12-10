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


def f(t, div=0, i=1):
    return i if div == len(t) else f(t, div+1, i*t[div]) + f(t, div+1, i)


def minus(num):
    return f(get_prime_divs(num))-1


print(minus(30))
