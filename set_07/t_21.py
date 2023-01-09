from t_06 import Node


def f(linked_list):
    pointer = linked_list.next
    shadow = linked_list
    current_subsequence_shadow = None
    longest_subsequence_shadow = None
    number_of_longest_subsequences = 1
    max_length = 0
    current_length = 1
    while pointer is not None:
        if pointer.val > shadow.val:
            current_length += 1
            if max_length < current_length:
                number_of_longest_subsequences = 1
                longest_subsequence_shadow = current_subsequence_shadow
                max_length = current_length
            elif max_length == current_length:
                number_of_longest_subsequences += 1
        else:
            current_subsequence_shadow = shadow
            current_length = 1
        shadow = pointer
        pointer = pointer.next
    if number_of_longest_subsequences == 1:
        remove(linked_list, longest_subsequence_shadow, max_length)


def remove(linked_list, shadow, elements):
    if shadow is None:
        pointer = linked_list
        for i in range(elements):
            pointer = pointer.next
        linked_list.val = pointer.val
        linked_list.next = pointer.next
    else:
        pointer = shadow
        for i in range(elements):
            pointer = pointer.next
        shadow.next = pointer.next


num_list = Node([1, 3, 5, 7, 9, 11, 12, 13, 3, 2, 1, 3, 5, 6, 7, 9, 11])
print(num_list)
print(f(num_list))
print(num_list)
