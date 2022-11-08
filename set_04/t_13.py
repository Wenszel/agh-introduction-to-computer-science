from random import randint


def sum_digits(number: int) -> int:
    output = 0
    while number >0:
        output += number % 10
        number //= 10
    return output


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    i = 2
    while i * i < number:
        if number % i == 0:
            return False
        i += 1
    return True


def f():
    n = int(input("n: "))
    t = [[randint(1, 10 ** 3) for _ in range(n)] for _ in range(n)]
    for i in t:
        for j in i:
            print(j, end=" ")
        print("")
    for y in range(n):
        for x in range(n):
            if not is_prime(sum_digits(t[y][x])):
                t[y][x] = 0
    print("------------------")
    for i in t:
        for j in i:
            print(j, end=" ")
        print("")


f()
