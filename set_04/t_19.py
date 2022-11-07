from random import randint
n = int(input("n: "))
t = [[randint(1, 20) for _ in range(n)] for _ in range(n)]
for i in t:
    for j in i:
        print(j, end=" ")
    print("")
k = int(input("k: "))
output = 0
moves = [-1 , 1]
for y in range(n):
    for x in range(n):
        for move in moves:
            diagonal = 1
            while 0 <= x + diagonal * move < n and 0 <= y + diagonal < n:
                if t[y + diagonal][x + (diagonal * move)] * t[y][x] == k:
                    output += 1
                diagonal += 1
print(output)