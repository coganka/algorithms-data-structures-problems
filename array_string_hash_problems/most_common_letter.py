def most_commonword(st):
    keys = {}
    most_common = 0
    most_common_char = ""
    for s in st:
        if s == ' ':
            continue
        s = s.lower()
        keys[s] = keys.get(s,0) + 1
        if keys[s] > most_common:
            most_common = keys[s]
            most_common_char = s
    
    return most_common_char