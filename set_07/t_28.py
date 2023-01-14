from t_06 import Node


def removed_in_ordered_list(value, ordered_list):
    shadow = None
    pointer = ordered_list
    while pointer is not None and pointer.val < value:
        shadow = pointer
        pointer = pointer.next
    if pointer is None:
        return False
    if pointer.val == value:
        if shadow is None:
            ordered_list.val = ordered_list.next.val
            ordered_list.next = ordered_list.next.next
        else:
            shadow.next = pointer.next
        return True
    else:
        return False


def remove_duplicates(ordered_list, non_ordered_list):
    p = non_ordered_list
    s = None
    removed_elements = 0
    while p is not None:
        if removed_in_ordered_list(p.val, ordered_list):
            removed_elements += 1
            if s is None:
                non_ordered_list.val = non_ordered_list.next.val
                non_ordered_list.next = non_ordered_list.next.next
                p = non_ordered_list
            else:
                s.next = p.next
        else:
            s = p
            p = p.next
    return removed_elements


list_1 = Node([1, 2, 4, 6, 7, 8, 10])
list_2 = Node([6, 4, 8, 1, 10, 11])
print(remove_duplicates(list_1, list_2))
print(list_1)
print(list_2)

