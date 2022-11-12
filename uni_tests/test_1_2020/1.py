def multi(t):
    biggest = 0
    for s in t:
        length = len(s)
        div = length // 2
        while div > 0:
            if length % div == 0:
                flag = True
                for i in range(length):
                    if s[i] != s[i % div]:
                        flag = False
                        break
                if flag:
                    break
            div -= 1
        if flag:
            biggest = max(len(s), biggest)
    return biggest


print(multi(["AAAAAAAAAA","ABABABABABABAB"]))