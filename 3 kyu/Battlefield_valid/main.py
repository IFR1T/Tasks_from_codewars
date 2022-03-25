def validate_battlefield(field):
    squares = []
    for i in range(10):
        for j in range(10):
            if field[i][j] == 1:
                squares.append(str(i) + str(j))
                if i != 0 and j != 0 and field[i - 1][j - 1] == 1 or i != 0 and j != 9 and field[i - 1][
                    j + 1] == 1 or i != 9 and j != 0 and field[i + 1][j - 1] == 1 or i != 9 and j != 9 and field[i + 1][
                    j + 1] == 1:
                    return False
    if len(squares) != 20:
        return False
    neib = {}
    ships = [0] * 4
    twos = []
    ones = []
    for square in squares:
        neib[square] = squares.count(str(int(square[0]) + 1) + square[1]) + squares.count(
            str(int(square[0]) - 1) + square[1]) + squares.count(square[0] + str(int(square[1]) + 1)) + squares.count(
            square[0] + str(int(square[1]) - 1))
        if neib[square] == 0:
            ships[0] += 1
        if neib[square] == 2:
            twos.append(square)
        else:
            ones.append(square)
    if ships[0] != 4 or len(twos) != 4:
        return False
    for square in ones:
        if str(int(square[0]) + 1) + square[1] in ones or str(int(square[0]) - 1) + square[1] in ones or square[
            0] + str(int(square[1]) + 1) in ones or square[0] + str(int(square[1]) - 1) in ones:
            ships[1] += 1
    if ships[1] != 3 * 2:
        return False

    return True

