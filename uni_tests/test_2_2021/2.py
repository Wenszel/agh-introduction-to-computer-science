def is_value_in_fib(value):
    a, b = 1, 1
    while b < value:
        a, b = b, a + b
    return b == value


def f(t):
    l = len(t)
    for r in range(l - 2):
        for c in range(l - 2):
            if is_value_in_fib(t[r][c]):
                if is_value_in_fib(t[r+1][c]):
                    i = 0
                    if t[r][c] + t[r+1][c] == t[r+2][c]:
                        print(t[r][c], t[r+1][c], end="", sep="")
                        while r + 2 + i < l and t[r+i][c] + t[r+1+i][c] == t[r+2+i][c]:
                            print(t[r+2+i][c], end="")
                            i += 1
                        return
                if is_value_in_fib(t[r][c+1]):
                    i = 0
                    if t[r][c] + t[r][c+1] == t[r][c+2]:
                        print(t[r][c], t[r][c+1], end="")
                    while c + 2 + i < l and t[r][c + i] + t[r][c + 1 + i] == t[r][c + 2 + i]:
                        print(t[r][c + 2 + i], end="")
                        i += 1

f([[1,1,1,1,1],[1,1,1,1,1],[2,1,1,1,1],[3,1,1,1,1],[5,1,1,1,1]])