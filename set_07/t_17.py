class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"<Node val:{self.val} next:{self.next}>"

    def add(self, val):
        head = self
        while head.next is not None:
            head = head.next
        new_node = Node(val)
        new_node.prev = head
        head.next = new_node


def ones_in_binary(decimal_number):
    ones = 0
    while decimal_number > 0:
        ones += decimal_number % 2
        decimal_number //= 2
    return ones


def f(linked_list):
    pointer = linked_list
    shadow = None
    while pointer is not None:
        if ones_in_binary(pointer.val) % 2 == 1:
            if shadow is not None:
                shadow.next = pointer.next
                if pointer.next is not None:
                    pointer.next.prev = shadow
        else:
            shadow = pointer
        pointer = pointer.next


num_list = Node(0)
num_list.add(1)
num_list.add(3)
num_list.add(2)
num_list.add(11)
print(num_list)
f(num_list)
print(num_list)
