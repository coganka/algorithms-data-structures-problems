def reverse_LL(head):
    cur = head
    next = None
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev