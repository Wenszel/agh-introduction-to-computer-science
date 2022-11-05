from random import randint
n = int(input("n: "))
t = [randint(1, 10 ** 5) for _ in range(n)]
max_el = 0
max_el_amount = 0
min_el = 10 ** 5
min_el_amount = 0
for i in range(n):
    if t[i] > max_el:
        max_el = t[i]
        max_el_amount = 1
    elif t[i] == max_el:
        max_el_amount += 1
    if t[i] < min_el:
        min_el = t[i]
        min_el_amount = 1
    elif t[i] == min_el:
        min_el_amount += 1

if min_el_amount == max_el_amount == 1:
    print(True)
else:
    print(False)
