suma = int(input())
a1 = a2 = b1 = b2 = 1
fib_sum = 1
while suma > fib_sum:
    fib_sum += a2
    a1, a2 = a2, a1 + a2
while suma < fib_sum:
    fib_sum -= b1
    b1, b2 = b2, b1 + b2
print(suma == fib_sum)
