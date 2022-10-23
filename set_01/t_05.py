eps = 1e-10
n = float(input())
side = n
while abs(side - n / side) > eps:
    side = (side + n / side) / 2
print(side)

