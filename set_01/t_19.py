eps = 1e-10
prev = 0
curr = 1
power = 1
i = 2

while abs(curr - prev) > eps:
    prev = curr
    curr += 1/power
    power *= i
    i += 1
print(curr)

