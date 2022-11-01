def f():
    n = int(input("n: "))
    for i in range(n + 1, 1000):
        fib_sum = 0
        a1 = b1 = a2 = b2 = 1
        while fib_sum < i:
            fib_sum += b1
            a1, b1 = b1, a1 + b1
        while fib_sum > i:
            fib_sum -= a2
            a2, b2 = b2, a2 + b2
        if fib_sum != n:
            return i


print(f())
