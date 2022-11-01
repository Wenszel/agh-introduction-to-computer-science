def calc_sum(n):
    return n * n + n + 1


def f():
    num = int(input())
    i = 1
    while calc_sum(i) <= num:
        if num % calc_sum(i) == 0:
            return True
        i += 1
    return False


print(f())
