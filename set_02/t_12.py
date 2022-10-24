def num_len(num):
    length = 0
    while num != 0:
        length += 1
        num //= 10
    return length


def num_check(num):
    length = num_len(num)
    while num != 0:
        if num % 10 == length:
            return True
        num //= 10
    return False


n = int(input())
print(num_check(n))
