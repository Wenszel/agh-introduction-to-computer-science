from t_06 import Node


def remove_divs(int_list):
    if int_list.val is None or int_list.next is None:
        return int_list
    shadow = int_list
    pointer = int_list.next
    output = Node()
    while pointer is not None:
        if pointer.val % shadow.val != 0:
            if output.val is None:
                output.val = shadow.val
            else:
                output.add(shadow.val)
        shadow = pointer
        pointer = pointer.next
    output.next = shadow.val
    return output


linked_list = Node([2, 422, 844, 322, 644])
print(linked_list)
linked_list = remove_divs(linked_list)
print(linked_list)
