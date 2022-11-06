from random import randint
n = int(input("Array length: "))
t = [[randint(1, 10 ** 5) for _ in range(n)] for _ in range(n)]
print("\nThe array:")
for i in t:
    for j in i:
        print(j, end=" ")
    print("")
max_sum_col = 0
max_col = -1
min_sum_row = 10 ** 10
min_row = -1
for y in range(n):
    sum_row = 0
    for x in range(n):
        sum_row += t[y][x]
    if sum_row < min_sum_row:
        min_row = y
        min_sum_row = sum_row
for x in range(n):
    sum_col = 0
    for y in range(n):
        sum_col += t[y][x]
    if sum_col > max_sum_col:
        max_col = x
        max_sum_col = sum_col

print("\nThe row and column of any element for which the quotient " 
      "of the sum of the elements in the column in which the "
      "element lies to the sum of the elements of the row in "
      "which the element lies is the largest.\n ", "x: ", max_col, "y: ", min_row)
