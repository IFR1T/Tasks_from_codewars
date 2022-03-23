def expand(expr):
    # Basic idea - turn expression to dict, and then multipy exprations by summarazing values for the same keys, where the key
    # is power of current x. First, we have to transform expration to dict, power and name of the 'x', I made special func for that

    def turn_to_dict(expr):
        exp = {}
        temp = expr.split('^')
        n = int(temp[1])
        temp[0] = temp[0].strip('()')
        temp_s = ''
        for i, c in enumerate(temp[0]):
            if c.isdigit() or c == '-':
                temp_s += c
            else:
                x = c
                exp[0] = int(temp[0][i + 1:])
                break

        if temp_s == '-':
            exp[1] = -1
        elif temp_s == '':
            exp[1] = 1
        else:
            exp[1] = int(temp_s)
        return exp, x, n

    # function for multipling different exprations. Works with any 2 exprations, that will speed up my pow func
    # main idea of this func - summarazing values for the same clues, where klue is the power of x, and value is coefficient.
    # when i multiply two powers - the product goes as value to the key that is sum of initial keys
    def mult(expr1, expr2):
        res = {}
        for key1, value1 in expr1.items():
            for key2, value2 in expr2.items():
                res[key1 + key2] = res.get(key1 + key2, 0) + value1 * value2
        return res

    # Recoure function for power expration. Uses mult function, and speed up proccess by multiplying in squares
    def pow(expr, n):
        if n == 0:
            return 1
        elif n == 1:
            return expr
        else:
            y = pow(expr, n // 2)
            y = mult(y, y)
            if n % 2:
                y = mult(y, expr)
            return y

    # Function to turn my dict back to expration
    def expand_text(exp, x):
        if exp == 1:
            return '1'
        res = ''
        for key in sorted(exp.keys(), reverse=True):
            if key != max(exp.keys()):
                res += ('' if exp[key] < 0 else '+')
            if key == 0:
                res += str(exp[key])
            elif exp[key] == 1:
                res += x
            elif exp[key] == -1:
                res += '-' + x
            else:
                res += str(exp[key]) + x
            if key > 1:
                res += '^' + str(key)
        return res

    exp, x, n = turn_to_dict(expr)
    exp = pow(exp, n)
    return expand_text(exp, x)


print(expand('(p-1)^3'))
c = input()
