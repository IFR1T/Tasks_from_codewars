def last_digit(n1, n2):
    d = {
        1: [1, 1, 1, 1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6, 4, 6],
        5: [5, 5, 5, 5],
        6: [6, 6, 6, 6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1, 9, 1],
        0: [0, 0, 0, 0]
    }
    return 1 if n2 == 0 else d[n1 % 10][(n2 - 1) % 4]