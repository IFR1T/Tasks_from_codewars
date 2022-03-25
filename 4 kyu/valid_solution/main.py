def valid_solution(board):
    for row in board:
        if len(set(row)) != 9:
            return False
        elif 0 in row:
            return False
    transp_board = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            transp_board[i][j] = board[j][i]
    for row in transp_board:
        if len(set(row)) != 9:
            return False
    box_board = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            box_board[i][j] = board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
    for row in box_board:
        if len(set(row)) != 9:
            return False
    return True