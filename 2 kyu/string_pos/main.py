
def find_position(string):
    for i in range(1, len(string) + 1):
        for j in range(i):
            temp = string[:i-j]
            n = j - i
            while n <= len(string) + 1:
                n += i
                if len(temp) < i:
                    if int(string[n + i - j: n + i - j + len(temp)]) == int(temp) + 1:
                        if n + i == len(string):
                            return [i, j]
                        else:
                            temp = string[n:n + i]
                    elif temp == len(temp) * '9' and string[n + i - j: n + i - j + len(temp)] == '0' * len(temp):
                        if string[n: n + len(temp) + 1] == str(10 ** len(temp)):
                            if n + i == len(string):
                                return [i, j]
                            else:
                                temp = string[n: n + i + 1]
                                i += 1
                        else:
                            if n + i == len(string):
                                return [i, j]
                            else:
                                temp = string[n:n + i]


                    else:
                        break
                elif temp == str('9' * len(temp)):
                    if string[n: n + len(temp) + 1] == str(10 ** len(temp)):
                        if n + i == len(string):
                            return [i, j]
                        else:
                            temp = string[n: n + i + 1]
                            i += 1
                else:
                    if n == 0:
                        continue
                    temp2 = string[n:n + i]
                    if int(temp2) == int(temp) + 1:
                        if n + i == len(string):
                            return [i, j]
                        else:
                            temp = temp2
                    else:
                        break
            else:
                return [i, j]

tests = ['789101112', '99100010011002', '99200201202', '9899100101102']
for t in tests:
    print(find_position(t))