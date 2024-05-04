def odd_even_LL(head):
    if not head:
        return None
    odd = head
    even = odd.next
    even_list = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_list
    return head