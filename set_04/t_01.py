def f():
    n = int(input("n: "))
    t = [[0 for _ in range(n)] for _ in range(n)]

    value = 1
    x = 0
    y = n - 1

    while x <= y:
        for j in range(x, y + 1):
            t[x][j] = value
            value += 1
        for i in range(x + 1, y):
            t[i][y] = value
            value += 1
        for j in range(y, x, -1):
            t[y][j] = value
            value += 1
        for i in range(y, x, -1):
            t[i][x] = value
            value += 1
        x += 1
        y -= 1

    for i in t:
        for j in i:
            print(j, end=" ")
        print("")


f()


