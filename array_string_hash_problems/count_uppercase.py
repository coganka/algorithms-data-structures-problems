def find_uppers(st):
    count = 0
    for s in st:
        if ord(s) >= 65 and ord(s) <= 90 :
            count += 1
    return count