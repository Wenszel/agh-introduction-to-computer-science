# Search in BST
def search(root,key):
    if root is None:
        return False
    if root.val == key: return True
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)
