from functools import reduce
def persistence(n):
    count = 0
    while n // 10 > 0:
        count += 1
        n = reduce(lambda x, y: int(x) * int(y), list(str(n)))
    return count