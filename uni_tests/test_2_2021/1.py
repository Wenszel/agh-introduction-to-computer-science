def gcp(a, b):
    if b == 0:
        return a
    return gcp(b, a % b)


T = [
    [3, 2, 4, 5],
    [2, 3, 4, 6],
    [2, 2, 3, 6],
    [2, 3, 5, 6],
]
n = len(T)

x = []


def moves_to_win(x,r1=0, c1=0, moves_counter=0):
    # if moves_counter >
    global T, n
    if r1 == c1 == n - 1:
        print('END', moves_counter)
        x.append(moves_counter)
        return moves_counter
    for i in range(r1 + 1, n):
        can_move = gcp(T[r1][c1], T[i][c1]) == 1
        if can_move:
            moves_to_win(x,i, c1, moves_counter + 1)
    for i in range(c1 + 1, n):
        can_move = gcp(T[r1][c1], T[r1][i]) == 1
        if can_move:
            moves_to_win(x,r1, i, moves_counter + 1)


print(moves_to_win(x))
print(list(set(x)))

y = []

def moves2_to_win(x,r1=0, c1=0, moves_counter=0):
    # if moves_counter >
    global T, n
    if moves_counter > 100:
        return False
    if r1 == c1 == n - 1:
        print('END', moves_counter)
        x.append(moves_counter)
        return moves_counter
    for i in range(r1 + 1, n):
        can_move = gcp(T[r1][c1], T[i][c1]) == 1
        if can_move:
            moves_to_win(x,i, c1, moves_counter + 1)

    for i in range(c1 - 1,-1,  -1):
        can_move = gcp(T[r1][c1], T[r1][i]) == 1
        if can_move:
            moves_to_win(x,r1, i, moves_counter + 1)


print(moves_to_win(x))
print(moves2_to_win(y))
print(list(set(x)))
print(list(set(y)))
res1 = min(x)
res2 = min(y)
print(0 if res1 == res2 else 1 if res1 < res2 else 2)
