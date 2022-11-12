def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def f(t):
    output = 0
    for i in range(len(t) - 2):
        j = [i + 1, i + 2]
        for elj in j:
            k = [elj + 1, elj + 2]
            for elk in k:
                if elj < len(t) and elk < len(t):
                    if nwd(nwd(t[i], t[elj]),t[elk]) == 1:
                        output += 1
    return output


print(f([1,2,3,4,5,6,7,8,9,10,14,12]))