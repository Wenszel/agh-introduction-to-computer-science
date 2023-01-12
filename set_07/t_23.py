from t_22 import element1


def cycle_length(linked_list):
    slow_pointer = linked_list
    fast_pointer = linked_list.next
    while slow_pointer != fast_pointer:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    slow_pointer = slow_pointer.next
    length = 1
    while slow_pointer != fast_pointer:
        length += 1
        slow_pointer = slow_pointer.next
    return length


print(cycle_length(element1))
