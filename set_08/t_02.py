# insert into BST
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if root.val < key:
        root.right = insert(root.right, key)
    if root.val > key:
        root.left = insert(root.left, key)
    return root
