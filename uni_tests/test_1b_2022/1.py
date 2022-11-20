def sequence(t):
    start = t[0]
    length = 1
    max_start = -1
    min_end = 99999
    for i in range(len(t) - 2):
        if t[i] < t[i+1]:
            length += 1
            end = t[i + 1]
        else:
            if length >= 3:
                max_start = max(max_start, start)
                min_end = min(min_end, end)
            length = 1
            start = t[i+1]
    return max_start > min_end


print(sequence([2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 1, 3, 2]))
print(sequence([2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 14, 3, 2]))


