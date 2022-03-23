def comp(array1, array2):
    if array1 is None or array2 is None or len(array1) != len(array2):
        return False

    while array1:
        num = array1[0]
        if num ** 2 in array2:
            array1.pop(0)
            array2.pop(array2.index(num ** 2))
        else:
            return False
    return True