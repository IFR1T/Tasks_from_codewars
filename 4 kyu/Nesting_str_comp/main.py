def same_structure_as(original,other):
    if type(original) != type(other):
        return False
    if len(original) == len(other) and all(map(lambda elem: type(elem) != list, original)) and all(map(lambda elem: type(elem) != list, other)):
        return True
    elif len(original) != len(other):
        return False
    else:
        for i in range(len(original)):
            if type(original[i]) == list:
                if type(other[i]) == list:
                    return same_structure_as(original[i], other[i])
                else:
                    return False