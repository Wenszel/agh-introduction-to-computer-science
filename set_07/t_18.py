from t_06 import Node


def remove_duplicates(linked_list):
    pointer = linked_list
    shadow = None
    while pointer is not None:
        pointer_2 = pointer.next
        while pointer_2 is not None:
            if pointer.val == pointer_2.val:
                if shadow is not None:
                    shadow.next = pointer.next
                else:
                    linked_list = linked_list.next
                break
            pointer_2 = pointer_2.next
        if pointer_2 is None:
            shadow = pointer
        pointer = pointer.next


num_list = Node([1, 3, 6, 7, 3, 6])
print(num_list)
remove_duplicates(num_list)
print(num_list)
