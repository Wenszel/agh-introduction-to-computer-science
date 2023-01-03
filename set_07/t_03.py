from t_01 import Node


def scal(l1, l2):
    if l1 is None or l1.val is None:
        return l2
    if l2 is None or l2.val is None:
        return l1
    if l1.val > l2.val:
        head = l2
        l2 = l2.next
    else:
        head = l1
        l1 = l1.next
    last = head
    while l1 is not None and l2 is not None:
        if l1.val > l2.val:
            last.next = l2
            l2 = l2.next
        else:
            last.next = l1
            l1 = l1.next
        last = last.next
    if l1 is None:
        last.next = l2
    if l2 is None:
        last.next = l1
    return head


list_a = Node(1)
list_a.add(3)
list_b = Node(4)
list_b.add(2)

print(scal(list_a, list_b))