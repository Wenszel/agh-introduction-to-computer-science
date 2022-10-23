def gcp(a, b):
    if b == 0:
        return a
    return gcp(b, a % b)


i = int(input("a: "))
j = int(input("b: "))
k = int(input("c: "))
print(gcp(gcp(i, j), k))
