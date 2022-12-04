def f(T, w, c=0,  i=0):
    if i == len(T) or w == c:
        return w == c
    return f(T, w, c + t[i], i + 1) or f(T, w, c, i + 1)


t = [1, 5, 3, 2, 7, 13, 2]
print(f(t, 21))