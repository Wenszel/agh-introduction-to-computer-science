def f(n1, n2):
    t = [False for _ in range(9)]
    if n1 > n2:
        n1, n2 = n2, n1
    while n1 > 0:
        t[n1 % 10] = True
        n1 //= 10
    while n2 > 0:
        if not t[n2 % 10]:
            return False
        n2 //= 10
    return True


num1 = int(input("n1: "))
num2 = int(input("n2: "))
print(f(num1, num2))