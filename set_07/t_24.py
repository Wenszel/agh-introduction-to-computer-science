from t_22 import element1


def before_cycle_length(linked_list):
    first_element_of_cycle = find_first_element_of_cycle(linked_list)
    pointer = linked_list
    length = 0
    while pointer != first_element_of_cycle:
        length += 1
        pointer = pointer.next
    return length


def find_first_element_of_cycle(linked_list):
    slow_pointer = linked_list
    fast_pointer = linked_list.next
    while slow_pointer != fast_pointer:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    slow_pointer = linked_list
    while slow_pointer != fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next
    return slow_pointer


print(before_cycle_length(element1))
