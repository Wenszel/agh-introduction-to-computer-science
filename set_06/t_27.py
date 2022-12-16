def f(t, total, squares, i):
    if i == len(t):
        return False
    if total == 2012 and len(squares) == 13:
        return True
    if not is_overlapping_square(t[i], squares):
        return f(t, total+square_surface(t[i]), len(squares) + 1, i + 1) or f(t, total, len(squares), i + 1)
    return f(t, total, len(squares), i + 1)


def square_surface(square):
    x = square[1] - square[0]
    y = square[3] - square[2]
    return x * y


def is_overlapping_square(checked_square, squares):
    for square in squares:
        if not (checked_square[1] < square[0] or checked_square[0] > square[1]):
            if not (checked_square[2] > square[3] or checked_square[3] < square[2]):
                return False
    return True
