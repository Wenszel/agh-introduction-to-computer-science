def hanoi(n, A, B, C):
    if n > 0:
        hanoi(n-1, A, C, B)
        C.insert(0, A.pop(0))
        hanoi(n-1, B, A, C)
