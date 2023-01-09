from t_06 import Node


def count_fives_in_octal(decimal_number):
    fives = 0
    while decimal_number > 0:
        if decimal_number % 8 == 5:
            fives += 1
        decimal_number //= 8
    return fives


def f(linked_list):
    pointer = linked_list
    shadow = None
    next_node = pointer
    while next_node is not None:
        next_node = next_node.next
        if count_fives_in_octal(pointer.val) % 2 == 0:
            if shadow is not None:
                shadow.next = pointer.next
                pointer.next = linked_list
                linked_list = pointer
        else:
            shadow = pointer
        pointer = next_node
    return linked_list


list_of_nums = Node([1, 14, 43, 23, 12, 44, 23, 32])
print(list_of_nums)
list_of_nums = f(list_of_nums)
print(list_of_nums)
