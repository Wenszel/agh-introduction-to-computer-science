from t_06 import Node


def f(linked_list, even_list, odd_list):
    shadow = None
    pointer = linked_list
    even_pointer = even_list
    odd_pointer = odd_list
    removed = 0
    while pointer is not None:
        if pointer.val % 2 == 0 and pointer.val > 0:
            if even_pointer.val is None:
                even_pointer.val = pointer.val
                even_pointer.next = None
            else:
                even_pointer.next = pointer
                even_pointer = even_pointer.next
            shadow = pointer
            pointer = pointer.next
        elif pointer.val % 2 == 1 and pointer.val < 0:
            if odd_pointer.val is None:
                odd_pointer.val = pointer.val
                odd_pointer.next = None
            else:
                odd_pointer.next = pointer
                odd_pointer = odd_pointer.next
            shadow = pointer
            pointer = pointer.next
        else:
            removed += 1
            if shadow is None:
                linked_list.val = pointer.next.val
                linked_list.next = pointer.next.next
                pointer = linked_list
            else:
                shadow.next = pointer.next
                shadow = pointer
                pointer = pointer.next
    even_pointer.next = None
    odd_pointer.next = None
    return removed


num_list = Node([1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4])
even = Node()
odd = Node()
print(f(num_list, even, odd))
print(even)
print(odd)
