def word_break(st, wordDict):
    res = []
    for i in range(len(wordDict)):
        copy = st[:]
        cur_str = ""
        for j in range(i, len(wordDict)):
            word = wordDict[j]
            if word in copy:
                copy = copy.replace(word, '')
                cur_str += word + " "
        res.append(cur_str)
    return res