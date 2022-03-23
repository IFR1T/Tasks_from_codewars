def solution(string, markers):
    text = string.split('\n')
    for i, word in enumerate(text):
        for mark in markers:
            word = word.split(mark)[0]
        text[i] = word.strip()
    return "\n".join(text)