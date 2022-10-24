def f():
    n = int(input())
    last = n % 10
    while n != 0:
        n //= 10
        if last == n % 10:
            return False
    return True


print(f())
