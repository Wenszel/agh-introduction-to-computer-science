from math import sqrt
def f(A, B):
    output = 0

    def r(a, b, num=1, ones=1, zeros=0):
        nonlocal output
        if a == ones and b == zeros:
            if is_bin_complex(num):
                output += 1
            return
        if ones < a:
            r(a, b, num * 10 + 1, ones+1, zeros)
        if zeros < b:
            r(a, b, num * 10, ones, zeros+1)
    r(A, B)
    return output


def is_bin_complex(num):
    dec = 0
    power = 0
    while num > 0:
        dec += (num % 10) * 2 ** power
        power += 1
        num //= 10
    for i in range(2, int(sqrt(dec) + 1)):
        if dec % i == 0:
            return True
    return False


print(f(2, 3))
