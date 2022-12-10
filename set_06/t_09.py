def f(t, weight,  i=0):
    if weight == 0:
        return True
    elif i == len(t):
        return False
    if f(t, weight, i+1):
        return True
    if f(t, weight + t[i], i+1):
        print("-", t[i])
        return True
    if f(t, weight - t[i], i+1):
        print(t[i])
        return True
    return False


t = [1, 5, 3, 2, 7, 13, 2]
print(f(t, 21))
