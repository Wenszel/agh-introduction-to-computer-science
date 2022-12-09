def f(t, k):
    def r(t, k, s1=0, s2=0, l1=0, l2=0, i=0):
        if i == len(t):
            return False
        else:
            if l1 + l2 == k:
                if s1 == s2:
                    return True
                else:
                    return False
            else:
                return r(t, k, s1, s2 + t[i], l1, l2+1, i+1) or r(t, k, s1 + t[i], s2, l1 + 1, l2, i + 1) or r(t, k, s1, s2, l1, l2, i + 1)

    return r(t, k)

print(f([1,3,7,2,5,3,11,8,3,4], 3))