
def find_position(string):
    for i in range(1, len(string) + 1):
        for j in range(i):
            temp = string[:i - j]
            n = -j
            res = int(string[i - j: i - j + i]) - 1
            count = 0
            while n <= len(string) + 1:
                n += i
                if len(temp) < i:
                    if int(string[n + j: n + j + len(temp)]) == int(temp) + 1:
                        if n + i == len(string):
                            return [i - count, j, i]
                        else:
                            temp = string[n:n + i]
                    elif temp == len(temp) * '9' and string[n + j: n + j + len(temp)] == '0' * len(temp):
                        if string[n: n + len(temp) + 1] == str(10 ** len(temp)):
                            if n + i == len(string):
                                return [i - count, j, i]
                            else:
                                temp = string[n: n + i + 1]
                                i += 1
                                count += 1
                        else:
                            if n + i == len(string):
                                return [i - count, j, i]
                            else:
                                temp = string[n:n + i]


                    else:
                        break
                elif temp == str('9' * len(temp)):
                    if len(string) < n + len(temp) + 1:
                        if string[n] == '1' and string[n+1:] == '0' * len(string[n+1:]):
                            return [i - count, j, i]
                        else:
                            break
                    elif string[n: n + len(temp) + 1] == str(10 ** len(temp)):
                        if n + i == len(string):
                            return [i - count, j, i]
                        else:
                            temp = string[n: n + i + 1]
                            i += 1
                            count += 1
                    else:
                        break
                elif len(string) < n + len(temp):
                    x = len(string) - n - len(temp)
                    if temp[:x] == string[n:]:
                        return [i - count, j, i]
                    elif int(temp[:x]) == int(string[n:]) - 1 and temp[x:] == '9' * len(temp[x:]):
                        return [i - count, j, i]
                    else:
                        break

                else:
                    if n == 0:
                        continue
                    temp2 = string[n:n + i]
                    if int(temp2) == int(temp) + 1:
                        if n + i == len(string):
                            return [i - count, j, i]
                        else:
                            temp = temp2
                    else:
                        break
            else:
                return [i - count, j, i]

#print(find_position('97989910'))
tests = ['31', '789101112', '99100010011002', '99200201202', '9899100101102', '7891011121', '979899100', '98999100', '3148073248',
         '555899959741198', '001']
res = []
for t in tests:
    print(find_position(t))
    i, j = find_position(t)[0], find_position(t)[1]
    start = (int(t[i - j: i + i - j]) - 1)
    res = 0
    x = 1
    print(start)
    while start:
        res += start % 10 * x
        x += 1
        start //= 10
    print(res + i - j - 2)