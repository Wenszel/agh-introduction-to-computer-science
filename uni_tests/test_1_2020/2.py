def distance(t):
    n = len(t)
    amount = 0
    biggest_index = -1
    while amount != 1:
        col = 0
        amount = 0
        for row in range(n):
            if t[row][col] == 1:
                amount += 1
                biggest_index = row
        col += 1
    amount = 0
    smallest_index = -1
    while amount != 1:
        col = 0
        amount = 0
        for row in range(n):
            if t[row][col] == 0:
                amount += 1
                smallest_index = row
    print(abs(biggest_index - smallest_index))
