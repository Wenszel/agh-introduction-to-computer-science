class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"<Node val:{self.val} next:{self.next}>"


def add(val, zb):
    if zb.val is None:
        zb.val = val
        return zb
    pointer = zb
    shadow = None
    while pointer is not None and val > pointer.val:
        shadow = pointer
        pointer = pointer.next
    if pointer is not None and pointer.val == val:
        if shadow is not None:
            shadow.next = pointer.next
        else:
            zb = pointer.next
        return zb
    new_node = Node(val)
    new_node.next = pointer
    if shadow is not None:
        shadow.next = new_node
    else:
        zb = new_node
    return zb


linked_set = Node(2)
linked_set = add(3, linked_set)
linked_set = add(6, linked_set)
linked_set = add(4, linked_set)
linked_set = add(4, linked_set)
linked_set = add(1, linked_set)
print(linked_set)
