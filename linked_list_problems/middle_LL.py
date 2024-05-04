def middle(head):
    if head is None:
        return None
    fast = head
    slow = head
    while fast.next:
        fast = fast.next
        slow = slow.next
        if fast.next == None:
            return slow
        else:
            fast = fast.next
    return None