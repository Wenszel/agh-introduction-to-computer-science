def every_factor_once(p):
    factor = 2
    last_factor = None
    while p > 1:
        if p % factor == 0:
            if factor == last_factor:
                return False
            p /= factor
            last_factor = factor
        else:
            factor += 1
    return True


t = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]
max_length = 0
for i in range(len(t)):
    if every_factor_once(t[i]):
        length = 1
        j = i + 1
        product = t[i]
        while j < len(t) and every_factor_once(product * t[j]):
            product *= t[j]
            length += 1
            j += 1
    max_length = max(length, max_length)
print(max_length)