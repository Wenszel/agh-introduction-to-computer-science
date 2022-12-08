import numpy as np


def place_queens(queens, row=0, col=0):
    if row == len(queens):
        print_chessboard(queens)
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


def print_chessboard(q):
    t = [['0' for _ in range(len(q))] for _ in range(len(q))]
    for r, c in q:
        t[r][c] = 'H'
    print(np.array(t))
    print(q)
    print('----------')


n = int(input("Enter the size of the chessboard: "))
place_queens([() for _ in range(n)])