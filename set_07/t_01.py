import copy


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"<Node val:{self.val} next:{self.next}>"

    def contains(self, searched_value):
        if self.is_empty():
            return False
        pointer = self
        while pointer.val is not None and pointer.val < searched_value:
            pointer = pointer.next
        return pointer.val is not None and pointer.val == searched_value

    def add(self, added_value):
        if self.is_empty():
            self.val = added_value
            return self
        pointer = self
        shadow = None
        while pointer is not None and pointer.val < added_value:
            shadow = pointer
            pointer = pointer.next
        if pointer is not None and pointer.val == added_value:
            return self
        new_node = Node(added_value)
        new_node.next = pointer
        if shadow is not None:
            shadow.next = new_node
        else:
            self.next = copy.deepcopy(pointer)
            self.val = added_value
        return self

    def is_empty(self):
        return self.val is None

    def delete(self, deleted_value):
        if self.is_empty():
            return self
        if self.val == deleted_value:
            if self.next is None:
                self.val = None
            else:
                self.val = self.next.val
                self.next = self.next.next
            return self
        pointer = self
        shadow = None
        while pointer is not None and pointer.val < deleted_value:
            shadow = pointer
            pointer = pointer.next
        if pointer is not None and pointer.val == deleted_value:
            if pointer.next is None:
                shadow.next = None
            else:
                shadow.next = pointer.next
        return self