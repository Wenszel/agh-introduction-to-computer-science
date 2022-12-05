def place_queens(queens, row=0, col=0):
    if row == len(queens):
        print(queens)
        return
    if col == len(queens):
        return
    if is_possible(queens, row, col):
        queens[row] = (row, col)
        place_queens(queens, row + 1)
    place_queens(queens, row, col + 1)


def is_possible(q, r, c):
    for i in range(r):
        (q_r, q_c) = q[i]
        if q_c == c or \
            q_c - q_r == c - r or \
            q_c + q_r == c + r:
            return False
    return True


n = int(input("Enter the size of the chessboard: "))
place_queens([() for _ in range(n)])