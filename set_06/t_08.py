def f(t, weight,  i=0):
    if weight == 0:
        return True
    elif i == len(t):
        return False
    else:
        return f(t, weight + t[i], i + 1) or f(t, weight - t[i], i + 1) or f(t, weight, i + 1)


t = [1, 5, 3, 2, 7, 13, 2]
print(f(t, 21))
