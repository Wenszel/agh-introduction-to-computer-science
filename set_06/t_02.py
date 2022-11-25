def p(t, s1, s2, s3, i):
    if i == len(t):
        return s1 == s2 == s3
    return p(t, s1 + weight(t[i]), s2, s3, i + 1) or \
           p(t, s1, s2 + weight(t[i]), s3, i + 1) or \
           p(t, s1, s2, s3 + weight(t[i]), i + 1)


def weight(n):
    output = 0
    i = 2
    while n > 0:
        if n % i == 0:
            output += 1
            while n % i == 0:
                n //= i
            i += 1
    return output
