import numpy as np


def f():
    t = [[-1 for _ in range(5)] for _ in range(5)]
    f_helper(pos=(0, 0), i=0, t=t)
    print(np.array(t))


def f_helper(t, pos, i):
    if i == len(t) ** 2:
        return True
    if not is_move_doable(t, pos):
        return False
    knight_moves = [(-1, 2), (-2, 1), (2, 1), (1, 2),
                    (-2, -1), (-1, -2), (1, -2), (2, -1)]
    t[pos[1]][pos[0]] = i
    for m in knight_moves:
        curr_pos = (pos[0] + m[0], pos[1] + m[1])
        if f_helper(t, curr_pos, i + 1):
            return True
    t[pos[1]][pos[0]] = -1
    return False


def is_move_doable(board, position):
    size = len(board)
    return 0 <= position[0] < size and 0 <= position[1] < size and board[position[1]][position[0]] == -1


f()

