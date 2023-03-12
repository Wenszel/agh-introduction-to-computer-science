from collections import deque
# Print tree with deque
def print_tree(p):
    if p is None:
        return
    s = deque()
    s.append(p)
    while len(s) > 0:
        a = s.pop()
        if a is None:
            print(a.val)
            s.append(a.left)
            s.append(a.right)