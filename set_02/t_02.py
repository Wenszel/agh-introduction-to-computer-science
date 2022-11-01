a = int(input('a: '))
b = int(input('b: '))
n = int(input('n: '))
print(a // b, "." if a % b != 0 else "", sep="", end="")
while n > 0:
    a *= 10
    print(a // b, end="")
    a %= b
    n -= 1

