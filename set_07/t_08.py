from t_01 import Node


def f(l):
    head = l
    while head.next is not None:
        if head.next.next is not None:
            tmp = head.next.next
            del head.next
            head.next = tmp
        head = head.next
    return l


l_test = Node(0)
for i in range(1, 48):
    l_test.add(i)
print(f(l_test))
