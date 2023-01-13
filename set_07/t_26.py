from t_06 import Node


def contains(checked_list, main_list):
    checked_list_pointer = checked_list
    main_list_pointer = main_list
    while checked_list_pointer is not None:
        contains_element = False
        while main_list_pointer is not None:
            if checked_list_pointer.val == main_list_pointer.val:
                contains_element = True
                break
        if not contains_element:
            return False
        main_list_pointer = main_list_pointer.next
        checked_list_pointer = checked_list_pointer.next
    return True


first_list = Node([1, 2, 3, 4, 5, 6])
second_list = Node([1, 2, 3, 4, 5, 6, 7])
third_list = Node([1, 2])
print(contains(first_list, second_list))
print(contains(third_list, first_list))
print(contains(second_list, third_list))
print(contains(second_list, first_list))
