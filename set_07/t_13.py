from t_06 import Node


def remove_smaller(int_list):
    if int_list.val is None or int_list.next is None:
        return int_list
    shadow = int_list
    tail_start = shadow
    pointer = int_list.next
    while pointer is not None:
        if shadow.val < pointer.val:
            tail_start = pointer
        elif shadow.val > pointer.val:
            tail_start.next = pointer.next
        shadow = pointer
        pointer = pointer.next
    return int_list


linked_list = Node([1, 342, 422, 31, 233, 55, 21])
print(linked_list)
linked_list = remove_smaller(linked_list)
print(linked_list)
