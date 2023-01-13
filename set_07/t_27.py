from t_06 import Node


def merge_rec(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val <= l2.val:
        result = l1
        result.next = merge_rec(l1.next, l2)
    else:
        result = l2
        result.next = merge_rec(l1, l2.next)
    return result


def merge(l1, l2):
    p1 = l1
    p2 = l2
    if p1.val <= p2.val:
        first_el = p1
        result = p1
        p1 = p1.next
    else:
        first_el = p2
        result = p2
        p2 = p2.next
    while p1 is not None and p2 is not None:
        if p1.val <= p2.val:
            result.next = p1
            p1 = p1.next
        else:
            result.next = p2
            p2 = p2.next
        result = result.next
    if p1 is None:
        while p2 is not None:
            result.next = p2
            result = result.next
            p2 = p2.next
    else:
        while p1 is not None:
            result.next = p1
            result = result.next
            p1 = p1.next
    return first_el


list_1 = Node([1, 5, 7, 8, 11, 22])
list_2 = Node([1, 2, 3, 4, 5, 8, 9, 10, 13])
print(merge(list_1, list_2))
print(merge_rec(list_1, list_2))
