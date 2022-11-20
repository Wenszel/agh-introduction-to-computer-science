from random import randint


def is_ones_quantity_odd(num):
    output = 0
    while num > 0:
        output += num % 10
        num //= 10
    return output % 2 == 1


def f(t):
    length = len(t)
    odd_ones_quantity = [[False for _ in range(length)] for _ in range(length)]
    for y in range(length):
        for x in range(length):
            odd_ones_quantity[y][x] = is_ones_quantity_odd(t[y][x])

    for row in range(length):
        array = odd_ones_quantity
        for i in range(length):
            array[row][i] = True
        for col1 in range(length):
            array[row][col1] = True
            for col2 in range(col1, length):
                array[row][col2] = True
                for i in odd_ones_quantity:
                    if not i:
                        return False
    return True
n = int(input("N: "))
t = [[randint(1, 10 ** 5) for _ in range(n)] for _ in range(n)]
print(f(t))