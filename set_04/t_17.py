from random import randint
n = int(input("n: "))
t = [[randint(1, 20) for _ in range(n)] for _ in range(n)]
for i in t:
    for j in i:
        print(j, end=" ")
    print("")
max_el = (-1 , -1)
max_value = 0
moves = [(-1, -1), (-1 , 1), (1, 1), (1, -1)]
for y in range(1, n - 1):
    for x in range(1, n - 1):
        value = 0
        for move in moves:
            value += t[y + move[0]][x+move[1]]
        if value > max_value:
            max_value = value
            max_el = (x, y)
print(max_el)