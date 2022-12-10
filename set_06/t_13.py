def rec(n, p=1, t=""):
    if n == 0:
        if len(t) > 2:
            print(t[:-1])

    for i in range(p, n+1):
        rec(n-i, i, t + str(i) + "+")


rec(4)
