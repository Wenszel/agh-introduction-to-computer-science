from random import randint


def sum_row(array, row):
    return sum(array[row])


def sum_column(array, column, n):
    output = 0
    for i in range(n):
        output = array[i][column]
    return output


n = int(input("n: "))
t = [[randint(1, 20) for _ in range(n)] for _ in range(n)]
for i in t:
    for j in i:
        print(j, end=" ")
    print("")

t_sum_max = 0
for i in range(n ** 2):
    for j in range(i + 1, n ** 2):
        i_row = i // n
        i_col = i % n
        j_row = j // n
        j_col = j % n
        if i_row == j_row:
            t_sum = sum_row(t, i_row) + sum_column(t, i_col, n) + sum_column(t, j_col, n) \
                    - 2 * t[i_row][i_col] - 2 * t[j_row][j_col]
        elif i_col == j_col:
            t_sum = sum_column(t, i_col, n) + sum_row(t, i_row) + sum_row(t, j_row) \
                    - 2 * t[i_row][i_col] - 2 * t[j_row][j_col]
        else:
            t_sum = sum_column(t, i_col, n) + sum_column(t, j_col, n) + sum_row(t, i_row) + sum_row(t, j_row) \
                    - (2 * t[i_row][i_col] + 2 * t[j_row][j_col] + t[i_row][j_col] + t[j_row][i_col])
        t_sum_max = max(t_sum_max, t_sum)
print(t_sum_max)