# Check if tree is AVL tree
def check(root):
    if root is None:
        return 0
    left = check(root.left)
    right = check(root.right)
    if left == -1 or right == -1:
        return -1
    if abs(left-right) <= 1:
        return max(left, right) + 1
    return -1
