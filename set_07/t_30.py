from t_06 import Node


def min_el(linked_list):
    output = None
    pointer = linked_list
    minimum = 9999
    while pointer is not None:
        if pointer.val < minimum:
            minimum = pointer.val
            output = pointer
        pointer = pointer.next
    return output


def remove_val(linked_list, val):
    shadow = None
    pointer = linked_list
    if linked_list.next is None:
        return None
    while pointer is not None:
        if pointer.val == val:
            if shadow is None:
                linked_list.val = pointer.next.val
                linked_list.next = pointer.next.next
            else:
                shadow.next = pointer.next
            return linked_list
        shadow = pointer
        pointer = pointer.next


def merge(list_1, list_2):
    output = None
    pointer = list_1
    while pointer is not None:
        min_of_list_2 = min_el(list_2)
        while list_2 is not None and min_of_list_2.val < pointer.val:
            if output is None:
                output = min_of_list_2
                result = min_of_list_2
            else:
                result.next = min_of_list_2
                result = result.next
            list_2 = remove_val(list_2, min_of_list_2.val)
            min_of_list_2 = min_el(list_2)
        if min_of_list_2 is not None and min_of_list_2.val == pointer.val:
            list_2 = remove_val(list_2, min_of_list_2.val)
        if output is None:
            output = pointer
            result = pointer
        else:
            result.next = pointer
            result = result.next
        pointer = pointer.next
    return output


l1 = Node([2, 3, 5, 7, 11])
l2 = Node([8, 2, 7, 4])
print(merge(l1, l2))
