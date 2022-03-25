
def find_position(string):
    for i in range(1, len(string) + 1):
        for j in range(i):
            temp = string[:i - j]
            n = -j
#            if temp == '9' * len(temp):
#                res = max(int(temp), int(string[i - j: 2 * i - j + 1]))
#            else:
#                res = max(int(temp), int(string[i - j: 2 * i - j]))
            count = 0
            while n < len(string) - i:
                n += i
                if len(temp) < i:
                    if int(string[n + j: n + j + len(temp)]) == int(temp) + 1:
                        if n + i == len(string):
                            return [i - count, j, res]
                        else:
                            temp = string[n:n + i]
                    elif temp == len(temp) * '9' and string[n + j: n + j + len(temp)] == '0' * len(temp):
                        if string[n: n + len(temp) + 1] == str(10 ** len(temp)):
                            if n + i == len(string):
                                return [i - count, j, temp]
                            else:
                                temp = string[n: n + i + 1]
                                i += 1
                                count += 1
                        else:
                            if n + i == len(string):
                                return [i - count, j, temp]
                            else:
                                temp = string[n:n + i]


                    else:
                        break
                elif temp == str('9' * len(temp)):
                    if len(string) < n + len(temp) + 1:
                        if string[n] == '1' and string[n+1:] == '0' * len(string[n+1:]):
                            return [i - count, j, temp]
                        else:
                            break
                    elif string[n: n + len(temp) + 1] == str(10 ** len(temp)):
                        if n + i == len(string):
                            return [i - count, j, temp]
                        else:
                            temp = string[n: n + i + 1]
                            i += 1
                            count += 1
                    else:
                        break
                elif len(string) < n + len(temp):
                    x = len(string) - n - len(temp)
                    if temp[:x] == string[n:]:
                        return [i - count, j, temp]
                    elif int(temp[:x]) == int(string[n:]) - 1 and temp[x:] == '9' * len(temp[x:]):
                        return [i - count, j, temp]
                    else:
                        break

                else:
                    if n == 0:
                        continue
                    temp2 = string[n:n + i]
                    if int(temp2) == int(temp) + 1:
                        if n + i == len(string):
                            return [i - count, j, temp]
                        else:
                            temp = temp2
                    else:
                        break
            else:
                if n + i < len(string):
                    return [i - count, j, temp]
                else:
                    reslist = [int(string[i:] + string[:i]) for i in range(len(string))]
                    return(0, 0, str(min(reslist)))


print(find_position('31'))
tests = ["456",
"454",
"455",
"910",
"9100",
"99100",
"00101",
"001",
"00",
"123456789",
"1234567891",
"123456798",
"10",
"53635",
"040",
"11",
"99",
"667",
"0404",
"949225100",
"58257860625",
"3999589058124",
"555899959741198",
"01",
"0910",
"0991",
"09910",
"09991", '99100', '789101112', '99100010011002', '99200201202', '9899100101102', '7891011121', '979899100', '98999100', '3148073248',
         '555899959741198', '001', '31']
for t in tests:
    j = find_position(t)[1]
    res = find_position(t)[2]
    while len(t) >= len(res):
        t = t[:t.find(res)]
        res = str(int(res) - 1)
    res = str(int(res) + 1)
    x = 1
    res1 = 0
    for i in range(len(res) - 1):
        res1 += 9 * 10 ** i * (i + 1)
    delta = int(res) - 10 ** (len(res) - 1)
    res1 += delta * len(res) + 1
    print(res1 - 1 - j)


"456"
"454"
"455"
"910"
"9100"
"99100"
"00101"
"001"
"00"
"123456789"
"1234567891"
"123456798"
"10"
"53635"
"040"
"11"
"99"
"667"
"0404"
"949225100"
"58257860625"
"3999589058124"
"555899959741198"
"01"
"0910"
"0991"
"09910"
"09991"