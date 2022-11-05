from math import sqrt
from random import randint


def is_first_factor(num, factor):
    if factor == 1:
        return False
    for i in range(2, int(sqrt(factor)) + 1):
        if factor % i == 0:
            return False
    return num % factor == 0


def is_possible(t, t_length, k):
    possible_moves = [False for _ in range(t_length)]
    for i in range(1, t_length - k):
        possible_moves[k + i] = is_first_factor(t[k + i], i)
    print("k = ", k, "possible moves: ", possible_moves)
    if k == t_length - 1:
        return True
    for j in range(k, t_length):
        if possible_moves[j]:
            k = j
            return is_possible(t, t_length, k)


def f():
    t_length = int(input("length of table: "))
    t = [randint(1, 10000) for _ in range(t_length)]
    print(t)
    print("Is possible? ", is_possible(t, t_length, 0))


f()

