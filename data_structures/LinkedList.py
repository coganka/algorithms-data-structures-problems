class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    # can also just hold tail variable
    def append(self, value):
        newNode = ListNode(value)
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
        
    def prepend(self, value):
        newNode = ListNode(value)
        temp = self.head
        self.head = newNode
        self.head.next = temp

    def remove(self, value):
        cur = self.head
        while cur.next:
            if cur.next.value == value:
                cur.next = cur.next.next
            cur = cur.next

    def display(self):
        cur = self.head
        while cur:
            print(cur.value, end=" -> ")
            cur = cur.next
        print("None")

    def remove_duplicate(self):
        cur = self.head
        unique_vals = [cur.value]
        while cur.next:
            if cur.next.value in unique_vals:
                cur.next = cur.next.next
            else:  
                unique_vals.append(cur.next.value)  
            cur = cur.next
        return self.display()
    
    def return_middle(self):
        if self.head is None or self.head.next is None:
            return self.head
        fast = self.head
        slow = self.head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next is None:
                break
            else:
                fast = fast.next
        return slow.value
        

# Example:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(4)
ll.prepend(6)
print(ll.return_middle())
ll.display()
ll.remove_duplicate()
print(ll.return_middle())