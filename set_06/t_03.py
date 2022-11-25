max_cost = 10 ** 10


def king(t, c, r=0, cost=0):
    o1 = o2 = o3 = max_cost
    if r == 8:
        return cost
    else:
        if c > 0:
            o1 = king(t, c - 1, r + 1, cost + t[r][c])
            o2 = king(t, c, r + 1, cost + t[r][c])
        if c < 7:
            o3 = king(t, c + 1, r + 1, cost + t[r][c])
        return min(o1, o2, o3)