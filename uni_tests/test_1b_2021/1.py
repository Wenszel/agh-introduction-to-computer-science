def f(T):
    index = None
    curr = 1
    for i in range(len(T)):
        if T[i] == curr and curr != 1:
            index = i
        if is_prime(T[i]):
            curr *= T[i]
    return index


def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i ** 2 < n:
        if n % i == 0:
            return False
        i += 1
    return True


print(f([2, 3, 5, 7, 6, 211]))
print(f([2, 3, 5, 7, 6, 210]))
