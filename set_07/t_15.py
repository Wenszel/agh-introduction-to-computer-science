#15. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej,
# usuwa z niej wszystkie elementy,
# w których wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.
from t_06 import Node


def dec_to_tri(num):
    output = 0
    power = 0
    while num > 0:
        output += num % 3 * 10 ** power
        power += 1
        num //= 3
    return output


def has_more_ones_than_twos(num_in_tri):
    ones = 0
    twos = 0
    while num_in_tri > 0:
        if num_in_tri%10 == 1:
            ones += 1
        elif num_in_tri%10 == 2:
            twos += 1
        num_in_tri //= 10
    return ones > twos


def remove_nums_with_more_ones(linked_list):
    pointer = linked_list
    shadow = None
    while pointer is not None:
        if has_more_ones_than_twos(dec_to_tri(pointer.val)):
            if shadow is not None:
                shadow.next = pointer.next
            else:
                linked_list = linked_list.next
        else:
            shadow = pointer
        pointer = pointer.next


num_list = Node([1, 23, 3,  12, 2, 42, 233, 321])
print(num_list)
remove_nums_with_more_ones(num_list)
print(num_list)
