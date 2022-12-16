def ones_in_binary(dec_num):
    output = 0
    while dec_num > 0:
        output += dec_num % 2
        dec_num //= 2

    return output


def r(t, s1=0, s2=0, s3=0, i=0):
    if i == len(t):
        return s1 == s2 == s3
    n = ones_in_binary(t[i])
    return r(t, s1 + n, s2, s3, i + 1) or r(t, s1, s2 + n, s3, i + 1) or r(t, s1, s2, s3 + n, i + 1)


print(r([2, 3, 5, 7, 15]))
print(r([5, 7, 15]))