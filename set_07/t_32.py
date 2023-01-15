from t_06 import Node


def subtraction(w1, w2):
    p1 = w1
    p2 = w2
    output = Node()
    while p1 is not None and p2 is not None:
        if output.val is None:
            output.val = p1.val - p2.val
        else:
            output.add(p1.val - p2.val)
        p1 = p1.next
        p2 = p2.next
    while p1 is not None:
        output.add(p1.val)
        p1 = p1.next
    while p2 is not None:
        output.add(p2.val)
        p2 = p2.next
    return output


def print_polynomial(w):
    output = ""
    power = 0
    p = w
    while p is not None:
        if p.val != 0:
            if power == 0:
                if p.val < 0:
                    output = " - "
                else:
                    output = " + "
                output += str(abs(p.val))
            else:
                if p.val < 0:
                    output = " - " + str(abs(p.val)) + "x^"+str(power) + str(output)
                else:
                    output = " + " + str(p.val) + "x^"+str(power) + str(output)
        p = p.next
        power += 1
    print(output[2:])


w_1 = Node([1, 23, 4, 3, 2, 1, 5])
w_2 = Node([3, 4, 1, 2, 3,4, 5, 5])
print_polynomial(w_1)
print_polynomial(w_2)
print_polynomial(subtraction(w_1, w_2))
