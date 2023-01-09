from t_06 import Node


def concat_intervals(i1, i2):
    i1, i2 = correct_intervals_order(i1, i2)
    if i1[1] >= i2[1]:
        return i1
    if i1[1] < i2[1]:
        return i1[0], i2[1]


def is_concat_possible(i1, i2):
    i1, i2 = correct_intervals_order(i1, i2)
    if i1[1] < i2[0] or i1[0] > i2[1]:
        return False
    return True


def correct_intervals_order(i1, i2):
    if i1[0] <= i2[0]:
        return i1, i2
    else:
        return i2, i1


def reduce_intervals(linked_list):
    pointer = linked_list
    while pointer is not None:
        shadow = pointer
        inner_pointer = pointer.next
        while inner_pointer is not None:
            if is_concat_possible(inner_pointer.val, pointer.val):
                pointer.val = concat_intervals(inner_pointer.val, pointer.val)
                shadow.next = inner_pointer.next
            else:
                shadow = inner_pointer
            inner_pointer = inner_pointer.next
        pointer = pointer.next


list_of_intervals = [(15, 19), (2, 5), (7, 11), (8, 12), (5, 6), (13, 17)]
intervals_list = Node(list_of_intervals)
print(intervals_list)
reduce_intervals(intervals_list)
print(intervals_list)
