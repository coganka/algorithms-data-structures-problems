def flatten(head):
    if not head:
        return None
    cur = head
    while cur:
        if cur.child is None:
            cur = cur.next
        else:
            tail = cur.child
            while tail.next != None:
                tail = tail.next
            tail.next = cur.next
            if tail.next is not None:
                tail.next.prev = tail
            cur.next = cur.child
            cur.child.prev = cur
            cur.child = None
    return head