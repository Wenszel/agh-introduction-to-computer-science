from t_06 import Node


def increment(l):
    tail = l
    head = l
    while head is not None:
        if head.val != 9:
            tail = head
        head = head.next
    if tail == l:

        first = Node(1)
        first.next = l
        tail.val = 0
        while tail.next is not None:
            tail = tail.next
            tail.val = 0
        return first
    else:
        tail.val += 1
        while tail.next is not None:
            tail = tail.next
            tail.val = 0
        return l


l = Node(9)
l.add(9)
l.add(9)
l.add(9)
l.add(9)
l.add(9)
l.add(9)
l.add(9)
print(l)
print(increment(l))