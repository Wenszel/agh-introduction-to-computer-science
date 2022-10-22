# A program that prints out elements of the Fibonacci sequence less than a million.
a, b = 1, 1
while a < 10 ** 6:
    print(a)
    a, b = b, a+b
