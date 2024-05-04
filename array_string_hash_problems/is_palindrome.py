def is_palindrome(st):
    st_list = list(st)
    res = []
    for s in st_list:
        if ord(s.lower()) >= 97 and ord(s.lower()) <= 122:
            res.append(s.lower())
    l, r = 0, len(res) - 1
    while l < r:
        if res[l] != res[r]:
            return False
        l += 1
        r -= 1
    return True
