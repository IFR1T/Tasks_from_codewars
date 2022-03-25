def rectangle_rotation(a, b):
    r2 = 2 ** 0.5
    board = int(abs(r2 * (a + b) / 4))
    count = 0
    for y in range(-max(a, b), max(a, b)):
        if y < r2 * a / 2 + board and y > -r2 * a / 2 + board and y < r2 * b / 2 - board and y > -r2 * b / 2 - board:
            count += 1
    if count == 0:
        board, count = board - 1, 2
    max_dot = 0
    for x in range(-max(a, b), max(a, b)):
        if 0 < r2 * a / 2 + x and 0 > -r2 * a / 2 + x and 0 < r2 * b / 2 - x and 0 > -r2 * b / 2 - x:
            max_dot += 1
    return ((board - (max_dot - 1) // 2) * 2 + 1) * max_dot + (max_dot - 1 + 2 * (count - 1)) * ((max_dot - 1) // 2)