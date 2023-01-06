class Node:
    def __init__(self, val=None):
        if isinstance(val, list):
            self.val = val[0]
            new_node = Node(val[1])
            self.next = new_node
            pointer = new_node
            for i in range(2, len(val)):
                nested_node = Node(val[i])
                pointer.next = nested_node
                pointer = nested_node
        else:
            self.val = val
            self.next = None

    def __repr__(self):
        return f"<Node val:{self.val} next:{self.next}>"

    def add(self, val):
        head = self
        while head.next is not None:
            head = head.next
        head.next = Node(val)
