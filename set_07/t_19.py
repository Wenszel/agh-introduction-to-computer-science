class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"<Node val:{self.val} next:{self.next}>"


def add(linked_list, added_value):
    pointer = linked_list
    shadow = None
    while pointer is not None and pointer.val < added_value:
        shadow = pointer
        pointer = pointer.next
    new_node = Node(added_value)
    new_node.next = pointer
    if shadow is not None:
        shadow.next = new_node
    else:
        return new_node
    return linked_list


def remove_duplicates(linked_list):
    pointer = linked_list
    shadow = None
    output = 0
    while pointer.next is not None:
        if pointer.val == pointer.next.val:
            output += 2
            pointer = pointer.next
            while pointer.val == pointer.next.val:
                output += 1
                pointer = pointer.next
            if shadow is None:
                linked_list.val = pointer.next.val
                linked_list.next = pointer.next.next
            else:
                shadow.next = pointer.next.next
        pointer = pointer.next
    return output


values = [1, 3, 6, 3, 7, 3, 6, 8, 9]
num_list = Node(1)
for value in values:
    num_list = add(num_list, value)
print(num_list)
print(remove_duplicates(num_list))
print(num_list)
