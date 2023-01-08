class Node:
    def __init__(self, string=None):
        self.string = string
        self.next = None

    def __repr__(self):
        return f"<Node val:{self.string} next:{self.next}>"


def add(set_list, string):
    if set_list.string is None:
        set_list.string = string
        return True
    pointer = set_list
    shadow = None
    while pointer is not None and is_alphabetically(string, pointer.string):
        shadow = pointer
        pointer = pointer.next
    if pointer is not None and string == pointer.string:
        return False
    if shadow is not None:
        new_node = Node(string)
        new_node.next = pointer
        shadow.next = new_node
    else:
        set_list.val(string)
        set_list.next = pointer
    return True


def is_alphabetically(string, compared_string):
    length = min(len(string), len(compared_string))
    for i in range(length):
        if string[i] > compared_string[i]:
            return True
        elif string[i] < compared_string[i]:
            return False
    if len(string) > len(compared_string):
        return True
    else:
        return False


string_list = Node('elo')
print(add(string_list, 'pomelo'))
print(add(string_list, 'pomelo'))
add(string_list, 'pomarańcza')
print(string_list)
