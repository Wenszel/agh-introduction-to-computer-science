def a(n):
    if n == 1:
        return 2
    return 3 * a(n-1) + 1


def f():
    num = int(input())
    i = 1
    while a(i) < num:
        if num % a(i) == 0:
            return True
        i += 1
    return False


print(f())
