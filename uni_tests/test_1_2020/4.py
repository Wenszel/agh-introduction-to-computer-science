from math import floor, log10


def to_bin(n):
    output = 0
    power = 0
    ones_quantity = 0
    while n > 0:
        output += n % 2 * 10 ** power
        ones_quantity += n % 2
        power += 1
        n //= 2
    return output, ones_quantity


def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def divide(n):
    for i in range(1, 2 ** (floor(log10(n)))):
        number = n
        mask, array_size = to_bin(i)
        array = [0 for _ in range(array_size + 1)]
        cut = 10
        index = 0
        while mask > 0:
            if mask % 10 == 1:
                array[index] = number % cut
                number //= cut
                index += 1
                cut = 10
            else:
                cut *= 10
            mask //= 10
        array[array_size] = number
        if is_prime(array_size + 1):
            flag = True
            for j in array:
                if not is_prime(j):
                    flag = False
            if flag:
                return True
    return False


print(divide(2137))