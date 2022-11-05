from random import randrange
n = int(input("length of table: "))
t = [randrange(1, 99, 2) for _ in range(n)]
max_len = 0
max_len_r_pos = 0
max_len_r_neg = 0
curr_len = 1
r = t[1] - t[0]
for i in range(1, n):
    if t[i] == t[i - 1] + r:
        curr_len += 1
    else:
        r = t[i] - t[i - 1]
        current_len = 1
    if max_len < curr_len:
        max_len = curr_len
        if r < 0:
            max_len_r_neg = r
        else:
            max_len_r_pos = r
print(max_len_r_pos - max_len_r_neg)