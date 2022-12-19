def rook(n, l):
    def r(w=0, k=0, i=0):
        nonlocal shortest
        if w == k == n - 1:
            shortest = min(shortest, i)
        for new_w in range(w+1, n):
            if l.count((new_w, k)) != 0:
                break
            r(new_w, k, i+1)
        for new_k in range(k + 1, n):
            if l.count((w, new_k)) != 0:
                break
            r(w, new_k, i + 1)
    shortest = n * 2
    r()
    return None if shortest == n * 2 else shortest


print(rook(8, [(0, 4), (1, 5), (2, 2), (2, 5), (3, 4), (4, 1),(4, 6),(5, 6), (6, 6), (7, 4)]))
print(rook(8, []))
print(rook(8, [(i, 1) for i in range(8)]))

