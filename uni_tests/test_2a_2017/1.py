#Dana jest tablica t[N][N] (reprezentuj¡ca szachownic¦)
# wypeaniona liczbami naturalnymi.
# Na szachownicy znajduj¡ si¦ dwie wie»e.
# Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie:
# czy istnieje ruch wie»¡ zwi¦kszaj¡cy sum¦ liczb na "szachowanych" przez wie»e polach?
# Do funkcji nale»y przekaza¢ tablic¦ oraz poao»enia dwóch wie», funkcja powinna zwróci¢ warto±¢ logiczn¡.
# Uwaga: zakaadamy, »e wie»a szachuje caay wiersz i kolumn¦ z wya¡czeniem pola, na którym stoi.
from random import randint
import numpy as np
t = [[randint(1, 9) for _ in range(4)] for _ in range(4)]
def f(chessboard, r1, c1, r2, c2):
    value = s(chessboard, r1, c1, r2, c2)
    print(np.array(chessboard))
    for i in range(4):
        print(value, s(chessboard, i, c1, r2, c2),
        s(chessboard, r1, i, r2, c2),
        s(chessboard, r1, c1, i, c2),
        s(chessboard, r1, c1, r2, i),)
        output = max(s(chessboard, i, c1, r2, c2),
        s(chessboard, r1, i, r2, c2),
        s(chessboard, r1, c1, i, c2),
        s(chessboard, r1, c1, r2, i), value)
        if output > value:
            return True

    return False

def s(chessboard, r1, c1, r2, c2):
    length = len(chessboard)
    output = 0
    if r1 != r2:
        for i in range(length):
            output += chessboard[r1][i]
            output += chessboard[r2][i]
        output -= chessboard[r1][c1] + chessboard[r2][c2]
    if c1 != c2:
        for i in range(length):
            output += chessboard[i][c1]
            output += chessboard[i][c2]
        output -= chessboard[r1][c1] + chessboard[r2][c2]
    if r1 == r2:
        for i in range(length):
            output += chessboard[r1][i]
        output -= chessboard[r1][c1] + chessboard[r2][c2]
    if c1 == c2:
        for i in range(length):
            output += chessboard[i][c1]
        output -= chessboard[r1][c1] + chessboard[r2][c2]
    if c1 != c2 and r1 != r2:
        output -= chessboard[r2][c1] + chessboard[r1][c2]
    return output

print(f(t, 0, 0, 3, 3))
print(f([[0,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,0]], 0, 0, 3, 3))