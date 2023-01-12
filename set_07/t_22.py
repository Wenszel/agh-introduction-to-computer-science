from t_06 import Node


def contains_cycle(linked_list):
    first_pointer = linked_list
    second_pointer = linked_list.next
    while second_pointer is not None:
        if first_pointer == second_pointer:
            return True
        first_pointer = first_pointer.next
        if second_pointer.next is not None:
            second_pointer = second_pointer.next.next
        else:
            second_pointer = None
    return False


element1 = Node(1)
last = element1
for i in range(2, 8):
    new_node = Node(i)
    last.next = new_node
    last = new_node
cycle_first = Node(8)
last.next = cycle_first
last = cycle_first
for i in range(9, 14):
    new_node = Node(i)
    last.next = new_node
    last = new_node
cycle_last = Node(14)
last.next = cycle_last
cycle_last.next = cycle_first
#print(contains_cycle(element1))
non_cycle_list = Node([1,2,3,4,5,6, 7])
#print(contains_cycle(non_cycle_list))