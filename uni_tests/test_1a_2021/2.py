def f(T):
    max_len = 0
    for i in range(0, len(T)):
        curr_len = 1
        for j in range(i + 1, len(T)):
            if same_digits(to_4(T[i]), to_4(T[j])):
                curr_len += 1
        if max_len < curr_len:
            max_len = curr_len

    return max_len


def same_digits(n1, n2):
    d1 = [False for _ in range(10)]
    d2 = [False for _ in range(10)]
    while n1 > 0:
        d1[n1 % 10] = True
        n1 //= 10
    while n2 > 0:
        d2[n2 % 10] = True
        n2 //= 10
    return d1 == d2


def to_4(num):
    output = 0
    power = 0
    print(num, end=" ")
    while num > 0:

        output += num % 4 * (10 ** power)
        power += 1
        num //= 4
    print(output)
    return output


print(f([13, 23, 23, 18,33,23]))