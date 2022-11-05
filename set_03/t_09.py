from random import randint
n = int(input("length of table: "))
t = [randint(1, 100) for _ in range(n)]
max_length = 0
current_length = 1
for i in range(1, n):
    if t[i] > t[i - 1]:
        current_length += 1
    else:
        current_length = 1
    if max_length < current_length:
        max_length = current_length
print(t)
print(max_length)
