from random import randint


def ones_in_bin(n):
    output = 0
    while n > 0:
        output += n % 2
        n //= 2
    return output


def is_condition(n1, n2):
    return ones_in_bin(n1) == ones_in_bin(n2)


def f(t1, t2):
    n1 = len(t1)
    n2 = len(t2)
    for y in range(n2 - n1):
        for x in range(n2 - n1):
            compatible = 0
            for i in range(n1):
                for j in range(n1):
                    if is_condition(t2[y+i][x+j],t1[i][j]):
                        compatible += 1
            if (compatible/n1**2)*100 > 33:
                return y, x


array1 = [[randint(1, 10 ** 5) for _ in range(3)] for _ in range(3)]
array2 = [[randint(1, 10 ** 5) for _ in range(20)] for _ in range(20)]
print(f(array1, array2))
