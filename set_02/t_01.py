def f():
    n = int(input())
    a1 = a2 = b1 = b2 = 1
    while a1 <= n:
        while b1 <= n:
            if a1*b1 == n:
                return True
            b1, b2 = b2, b1 + b2
        b1 = b2 = 1
        a1, a2 = a2, a1 + a2
    return False


print(f())
