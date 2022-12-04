t = [1, 7, 3, 5, 11, 2]
output = 999
min_length = len(t)


def f(T, s=0, s_i=0, i=0, length=0):
    global output, min_length
    if i == len(T):
        if s == s_i and min_length > length > 0:
            min_length = length
            output = min(output, s)
        return
    return f(T, s, s_i, i + 1, length) or f(T, s+T[i], s_i + i, i + 1, length + 1)


f(t)
print(output)
