def move_zeros(array):
    n, i = 0, 0
    while n < len(array) - 1:
        n += 1
        if array[i] == 0:
            array.append(array.pop(i))
        else:
            i += 1
    return array
