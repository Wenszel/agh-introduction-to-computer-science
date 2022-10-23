year = int(input("Enter the current year: "))
min_sum = year + 1
out_a, out_b = 1, 1
for a in range(1, year):
    for b in range(a, year):
        fib_a, fib_b = a, b
        while fib_a + fib_b < year:
            fib_a, fib_b = fib_b, fib_a + fib_b
        if fib_a+fib_b == year:
            if a+b < min_sum:
                min_sum = a + b
                out_a, out_b = a, b
print(out_a, out_b)
