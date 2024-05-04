def is_palindrome_queue(st):
    queue = []
    for s in st:
        queue.append(s)
    i = len(st)-1
    while len(queue) > 0:
        cur = queue.pop(0)
        if st[i] != cur:
            return False
        i -= 1
    return True