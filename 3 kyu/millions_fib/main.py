def multm(a, b):
    res = [[[]] * 2 for _ in range(2)]
    res[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
    res[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
    res[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
    res[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
    return res


def powm(x, n):
    if x == 0:
        return [[1] * 2 for _ in range(2)]
    elif n == 1:
        return x
    else:
        y = powm(x, n // 2)
        y = multm(y, y)
        if n % 2:
            y = multm(y, x)
        return y


def fib(n):
    if n == 0:
        return 0
    elif abs(n) == 1:
        return 1
    else:
        res = powm([[1, 1], [1, 0]], abs(n) - 1)[0][0]
        if n > 0 or n % 2 == 1:
            return res
        else:
            return -res