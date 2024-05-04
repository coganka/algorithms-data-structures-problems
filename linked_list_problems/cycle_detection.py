def cycle(head):
    if head is None or head.next is None:
        return False
    fast = head
    slow = head
    while fast.next:
        fast = fast.next
        slow = slow.next
        if fast is None or fast.next is None:
            return False
        else:
            fast = fast.next
        if fast == slow:
            break
    p1 = head
    p2 = slow
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p2