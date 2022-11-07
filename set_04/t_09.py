from random import randint


def length_of_array(array):
    length = 0
    for _ in array:
        length += 1
    return length


def f(t, k):
    l = length_of_array(t)
    for y in range(l):
        for x in range(l):
            diag = 1
            while 0 < y + diag < l and 0 < x + diag < l:
                value = t[y+diag][x+diag] \
                        * t[y-diag][x+diag]\
                        * t[y+diag][x-diag]\
                        * t[y-diag][x-diag]
                if value == k:
                    return True, x, y, diag
                diag += 1
    return False


N = int(input("N: "))
t = [[randint(1, 9) for _ in range(N)] for _ in range(N)]
for i in t:
    for j in i:
        print(j, end=" ")
    print("")
k = int(input("k: "))
print(f(t, k))