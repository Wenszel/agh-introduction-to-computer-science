from random import randint


def is_prime(number: int) -> bool:
    if number == 1:
        return False
    i = 2
    while i * i < number:
        if number % i == 0:
            return False
        i += 1
    return True


def is_any_digit_prime(number: int) -> bool:
    while number > 0:
        if is_prime(number % 10):
            return True
        number //= 10
    return False


def f():
    n = int(input("n: "))
    t = [[randint(1, 10 ** 3) for _ in range(n)] for _ in range(n)]
    for i in t:
        for j in i:
            print(j, end=" ")
        print("")
    for y in range(n):
        flag = True
        for x in range(n):
            if is_any_digit_prime(t[y][x]):
                flag = False
        if flag:
            return flag
    return False


print(f())