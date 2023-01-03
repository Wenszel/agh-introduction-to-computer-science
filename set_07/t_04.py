from t_01 import Node


def reverse(l):
    if l is None:
        return None
    if l.next is None:
        return l

    p = None
    q = l
    curr = q.next
    print("p: ", p, "\nq:", q ,'\ncurr:', curr)
    while q is not None:
        q.next = p
        p = q
        q = curr
        if curr is not None:
            curr = curr.next
        print("p: ", p, "\nq:", q ,'\ncurr:', curr)
    return p


list_a = Node(1)
for i in range(2, 10):
    list_a.add(i)
print(reverse(list_a))
