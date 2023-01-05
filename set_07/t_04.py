def reverse(linked_list):
    result = None
    pointer = linked_list
    remaining = pointer.next
    while pointer is not None:
        pointer.next = result
        result = pointer
        pointer = remaining
        if remaining is not None:
            remaining = remaining.next
    return result
