k = int(input())
step = (k - 1) / 100_000
surface = 0
while k > 1:
    k -= step
    surface += 1 / k * step
print(surface)

