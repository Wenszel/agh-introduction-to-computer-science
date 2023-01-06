def div(linked_list):
    starts = [None for _ in range(10)]
    ends = [None for _ in range(10)]
    while linked_list is not None:
        i = linked_list.val % 10
        if starts[i] is None:
            starts[i] = linked_list
            ends[i] = linked_list
        else:
            ends[i].next = linked_list
            ends[i] = linked_list
        linked_list = linked_list.next

    result = None
    for i in range(9, -1, -1):
        if starts[i] is not None:
            ends[i].next = result
            result = starts[i]
    return result
