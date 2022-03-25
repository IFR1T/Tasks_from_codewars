def format_duration(seconds):
    if seconds == 0:
        return 'now'
    res = [0] * 5
    ress = ''
    vars = ['year', 'day', 'hour', 'minute', 'second']
    res[0], tale = seconds // (365 * 24 * 60 * 60), seconds % (365 * 24 * 60 * 60)
    res[1], tale = tale // (24 * 60 * 60), tale % (24 * 60 * 60)
    res[2], tale = tale // (60 * 60), tale % (60 * 60)
    res[3], res[4] = tale // 60, tale % 60
    for i, num in enumerate(res):
        if num > 0:
            ress += f'{num} {vars[i]}'
            if num > 1:
                ress += 's'
            if len(list(filter(lambda x: x > 0, res[i + 1:]))) == 1:
                ress += ' and '
            if len(list(filter(lambda x: x > 0, res[i + 1:]))) > 1:
                ress += ', '
    return ress