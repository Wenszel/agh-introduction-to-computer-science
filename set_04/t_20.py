from random import randint

n = int(input("n: "))
t = [[randint(1, 20) for _ in range(n)] for _ in range(n)]
for i in t:
    for j in i:
        print(j, end=" ")
    print("")

t_sum_max = 0
sc = [0 for _ in range(n)]
sr = [0 for _ in range(n)]
for x in range(n):
    for y in range(n):
        sc[x] += t[x][y]
        sr[x] += t[y][x]

for i in range(n ** 2):
    for j in range(i + 1, n ** 2):
        i_row = i // n
        i_col = i % n
        j_row = j // n
        j_col = j % n
        if i_row == j_row:
            t_sum = sr[i_row] + sc[i_col] + sc[j_col] \
            - 2 * t[i_row][i_col] - 2 * t[j_row][j_col]
        elif i_col == j_col:
            t_sum = sc[i_col] + sr[i_row] + sr[j_row] \
                    - 2 * t[i_row][i_col] - 2 * t[j_row][j_col]
        else:
            t_sum = sc[i_col] + sc[j_col] + sr[i_row] + sr[j_row] \
                    - (2 * t[i_row][i_col] + 2 * t[j_row][j_col] + t[i_row][j_col] + t[j_row][i_col])
        t_sum_max = max(t_sum_max, t_sum)
print(t_sum_max)