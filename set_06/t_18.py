'''
Zadanie 18. W szachownicy o wymiarach 8x8 kazdemu z pól przypisano liczbe naturalna. Na ruchy króla
nałozono dwa ograniczenia: król moze przesunac sie na jedno z 8 sasiednich pól jezeli ostatnia cyfra liczby na
polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
(np. naroznika) król nie moze wykonac ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
T[8][8] wypełniona liczbami naturalnymi reprezentujaca szachownice. Lewy górny naroznik ma współrzedne
w=0 i k=0. Prosze napisac funkcje sprawdzajaca czy król moze dostac sie z pola w,k do prawego dolnego
naroznika.
'''

from random import randrange
import math
from copy import deepcopy

def length(a):
    return math.floor(math.log10(a)) + 1


n = 8
t = [[32, 11, 6, 2, 3, 3, 16, 5],
     [11, 11, 6, 2, 3, 3, 16, 5],
     [33, 22, 32, 34, 3, 2, 1, 6],
     [44, 2, 31, 4, 17, 13, 11, 33],
     [55, 86, 7, 43, 8, 9, 12, 76],
     [66, 3, 2, 6, 52, 96, 8, 87],
     [77, 31, 39, 76, 7, 83, 82, 22],
     [88, 6, 9, 13, 17, 28, 88, 97]]


def get_first_digit(number):
    return number // (10 ** (length(number) - 1))

def get_last_digit(num):
    return num % 10

def czy_mozliwe(w, k, next_w, next_k):
    global t
    n = len(t)
    if 0 <= next_w <= n - 1 and 0 <= next_k <= n - 1:
        if get_last_digit(t[w][k]) < get_first_digit(t[next_w][next_k]):
            return True
    return False


def king_walk(w=0, k=0, droga=[]):
    global t, n
    if w == n - 1 and k == n - 1:
        return True
    else:
        moves = [(1, 0), (1, 1), (0, 1)]
        for move in moves:
            next_w = w + move[0]
            next_k = k + move[1]
            if czy_mozliwe(w, k, next_w, next_k) and king_walk(next_w, next_k, droga):
                # print(t[next_w][next_k])
                return king_walk(next_w, next_k, droga+[t[next_w][next_k]])
                # return True
    return False

print(king_walk())