from random import randint
t = [[randint(1, 10) for _ in range(8)] for _ in range(8)]

def is_prime(num):
    i = 2
    while num > i * i:
        if num % i == 0:
            return False
        i += 1
    return True
def f(chessboard, n):
    for r in range(n-1):
        for c in range(n-1):
            knight1_value = chessboard[r][c]
            i = 1
            while r+i < n and c+i < n:
                knight2_value = chessboard[r+i][c+i]
                if is_prime(knight1_value+knight2_value):
                    return True
    return False

