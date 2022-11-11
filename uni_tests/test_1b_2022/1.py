def sequence(t):
    sub = [[] for _ in range(len(t)//3)]
    mini = t[0]
    index = 0
    length = 1
    for i in range(len(t) - 2):
        if t[i] < t[i+1]:
            length += 1
            maxi = t[i + 1]
        else:
            if length >= 3:
                sub[index] = (mini,maxi)
                index += 1
            length = 1
            mini = t[i+1]
    for i in sub:
        for j in sub:
            if len(i) > 0 and len(j) > 0:
                if i[1] < j[0] or j[1] < i[0]:
                    return True
    return False


print(sequence([2,15,17,13,17,19,23,2,6,4,8,3,5,7,1,3,2]))
print(sequence([2,15,17,13,17,19,23,2,6,4,8,3,5,7,14,3,2]))


