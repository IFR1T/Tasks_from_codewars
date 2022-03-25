def increment_string(strng):
    num = ''
    for c in strng[::-1]:
        if not c.isdigit():
            break
        else:
            num += c
    if num == '':
        strng += '1'
    else:
        strng = strng[:len(strng) - len(num)] + '0' * (len(num) - len(str(int(num[::-1]) + 1))) + str(int(num[::-1]) + 1)
    return strng