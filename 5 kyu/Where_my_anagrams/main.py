def anagrams(word, words):
    res = []
    word_list = sorted(list(word))
    for wrd in words:
        if sorted(list(wrd)) == word_list:
            res.append(wrd)
    return res

