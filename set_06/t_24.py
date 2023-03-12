from math import sqrt


def f(t):
    smallest = 999999
    am = 0


    def r(x1=0, y1=0, l1=0, x2=0, y2=0, l2=0, i=0):
        nonlocal smallest
        if i == len(t):
            if l1 > 0 and l2 > 0:
                s1 = center_of_gravity(x1, y1, l1)
                s2 = center_of_gravity(x2, y2, l2)
                smallest = min(smallest, distance(s1, s2))
            return
        r(x1, y1, l1, x2, y2, l2, i+1)
        r(x1+t[i][0], y1+t[i][1], l1+1, x2, y2, l2, i+1)
        r(x1, y1, l1, x2+t[i][0], y2+t[i][1], l2+1, i+1)
        r(x1+t[i][0], y1+t[i][1], l1+1, x2+t[i][0], y2+t[i][1], l2+1, i+1)

    def distance(s1, s2):
        return sqrt((s1[0] + s2[0])**2 + (s1[1] + s2[1])**2)

    def center_of_gravity(x, y, l):
        return x/l, y/l

    r()
    return smallest


print(f([(1,1), (2,1)]))

