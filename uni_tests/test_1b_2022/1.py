def sequence(t):
    sub_seq = [[] for _ in range(len(t)//3)]
    sub_seq_i = 0
    start = t[0]
    length = 1
    for i in range(len(t) - 2):
        if t[i] < t[i+1]:
            length += 1
            end = t[i + 1]
        else:
            if length >= 3:
                sub_seq[sub_seq_i] = (start, end)
                sub_seq_i += 1
            length = 1
            start = t[i+1]
    for i in sub_seq:
        for j in sub_seq:
            if len(i) > 0 and len(j) > 0:
                if i[1] < j[0] or j[1] < i[0]:
                    return True
    return False


print(sequence([2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 1, 3, 2]))
print(sequence([2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 14, 3, 2]))


