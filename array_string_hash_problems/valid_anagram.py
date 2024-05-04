def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    hash = {}
    for i in range(len(s)):
        if s[i] not in hash:
            hash[s[i]] = 1
        else:
            hash[s[i]] += 1
    for i in range(len(t)):
        if t[i] not in hash:
            return False
        else:
            hash[t[i]] -= 1
        if hash[t[i]] == 0:
            del hash[t[i]]
    return len(hash) == 0