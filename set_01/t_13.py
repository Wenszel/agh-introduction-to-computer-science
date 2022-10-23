def gcp(a, b):
    if b == 0:
        return a
    return gcp(b, a % b)


def lcm(a, b):
    return a*b / gcp(a, b)


i = int(input("a: "))
j = int(input("b: "))
k = int(input("c: "))
print(lcm(lcm(i, j), k))
