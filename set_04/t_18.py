from random import randint
n = int(input("n: "))
t = [[randint(1, 20) for _ in range(n)] for _ in range(n)]
for i in t:
    for j in i:
        print(j, end=" ")
    print("")
max_sum = 0
for y in range(n):
    for x in range(n):
        # Horizontal
        curr_sum = 0
        for i in range(10):
            if not 0 < y < n or not 0 < x + i < n:
                break
            curr_sum += t[y][x + i]
            max_sum = max(max_sum, curr_sum)
        # Vertical
        curr_sum = 0
        for i in range(10):
            if not 0 < y + i < n or not 0 < x < n:
                break
            curr_sum += t[y + i][x]
            max_sum = max(max_sum, curr_sum)
print(max_sum)
