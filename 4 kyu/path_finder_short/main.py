def path_finder(maze):
    def line_update(maze, checked, i, j, line):
        dif = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        for l, m in dif:
            if 0 <= (i + l) < n and 0 <= (j + m) < n and maze[i + l][j + m] == '.' and (i + l, j + m) not in checked and (i + l, j + m) not in line:
                line.append((i + l, j + m))
                steps[(i + l, j + m)] = steps[(i, j)] + 1
        checked.append((i, j))
        line.pop(0)
        return(line)


    maze_l = [list(c) for c in maze.split('\n')]
    n = len(maze_l)
    line = [(0, 0)]
    steps = {(0, 0): 0}
    checked = []
    while line:
        i, j = line[0]
        if i == j == n - 1:
            return steps[(i, j)]
        line = line_update(maze_l, checked, i, j, line)
    return False