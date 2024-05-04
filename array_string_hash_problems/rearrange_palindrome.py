def arrange_palindrome(st):
    keys = {}
    res = []
    single_flag = False
    single_char = ""
    for s in st:
        keys[s] = keys.get(s,0) + 1
    for k, v in keys.items():
        if v > 1:
            while v > 0:
                res.insert(0,k)
                res.append(k)
                v -= 2
                keys[k] -= 2
        elif v == 1 and single_flag is False:
            single_char = k
            single_flag = True
    mid = len(res) // 2
    res.insert(mid, single_char)
    return res