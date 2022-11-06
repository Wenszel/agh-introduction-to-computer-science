from random import randint
n = int(input("Array length: "))
t = [[randint(- 10 ** 5, 10 ** 5) for _ in range(n)] for _ in range(n)]
print("\nThe array:")
for i in t:
    for j in i:
        print(j, end=" ")
    print("")


min_sum_row = None
min_row = -1
min_sum_row_abs = None
min_row_abs = -1
for y in range(n):
    sum_row = 0
    for x in range(n):
        sum_row += t[y][x]
    if min_sum_row is None or sum_row < min_sum_row:
        min_row = y
        min_sum_row = sum_row
    if min_sum_row_abs is None or abs(sum_row) < min_sum_row_abs:
        min_row_abs = x
        min_sum_row_abs = abs(sum_row)

max_sum_col = None
max_col = -1
max_sum_col_abs = None
max_col_abs = -1
for x in range(n):
    sum_col = 0
    for y in range(n):
        sum_col += t[y][x]
    if max_sum_col is None or sum_col > max_sum_col:
        max_col = x
        max_sum_col = sum_col
    if max_sum_col_abs is None or abs(sum_col) > max_sum_col_abs:
        max_col_abs = x
        max_sum_col_abs = abs(sum_col)


print("\nThe row and column of any element for which the quotient " 
      "of the sum of the elements in the column in which the "
      "element lies to the sum of the elements of the row in "
      "which the element lies is the largest: ")
if max_sum_col_abs / min_sum_row_abs > max_sum_col / min_sum_row:
    print("row: ", min_row_abs, "column: ", max_col_abs)
else:
    print("row: ", min_row, "column: ", max_col)
