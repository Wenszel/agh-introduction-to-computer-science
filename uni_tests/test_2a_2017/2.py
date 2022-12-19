def is_prime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i +=1
    return True


def r(t=[1, 0, 0, 0, 0, 0, 0,  0, 0], d=[i for i in range(2, 10)], i=1):
    if i == len(t):
        print(t)
    for index in range(len(d)):
        if d[index] != 0:
            if abs(d[index] - t[i-1]) >= 2:
                if not is_prime(t[i-1]) or not is_prime(d[index]):
                    t[i] = d[index]
                    d[index] = 0
                    r(t, d, i+1)


r()
