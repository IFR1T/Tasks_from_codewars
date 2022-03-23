res = [0]

def fibonacci(n):
    if n < len(res):
        return res[n]
    if n in [0, 1]:
        global res0, res1
        res0, res1 = 0, 1
        res.append(1)
        return n
    fibonacci(n - 1)
    res0, res1 = res1, res0 + res1
    res.append(res1)
    return res1