n = int(input())
s = 0
k = 1
while k <= n:
    j = k
    while j <= n:
        i = j
        while i <= n:
            s += 1
            i *= 5
        j *= 3
    k *= 2
print(s)