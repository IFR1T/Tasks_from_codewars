def in_array(array1, array2):
    res = []
    strneeded = ' '.join(array2)
    array1 = list(set(array1))
    for word in array1:
        if word in strneeded:
            res.append(word)
    return sorted(res)
