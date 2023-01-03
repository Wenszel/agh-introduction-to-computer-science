class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"<Node val:{self.val} next:{self.next}>"

    def add(self, val):
        head = self
        while head.next is not None:
            head = head.next
        head.next = Node(val)


