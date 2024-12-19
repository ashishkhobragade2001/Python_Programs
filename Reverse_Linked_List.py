class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Example usage
head = ListNode(1, ListNode(2, ListNode(3)))
reversed_list = reverse_linked_list(head)

# Printing reversed list
while reversed_list:
    print(reversed_list.value, end=" ")
    reversed_list = reversed_list.next
# Output: 3 2 1
