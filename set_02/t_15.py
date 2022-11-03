def is_correct(num, power):
    f_sum = 0
    i = num
    while i > 0:
        f_sum += (i % 10) ** power
        i //= 10
    return f_sum == num


n = int(input())
for i in range(10 ** (n - 1), 10 ** n):
    if is_correct(i, n):
        print(i)