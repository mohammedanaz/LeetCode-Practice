# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)  # A dummy head to simplify the code
        current = dummy_head
        carry = 0
        
        # Traverse both lists
        while l1 or l2:
            # Get the values of the current nodes (if they exist)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Compute the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry
            current.next = ListNode(total % 10)  # Create a new node with the sum modulo 10
            
            # Move to the next nodes in the lists
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # If there's a remaining carry, create a new node for it
        if carry > 0:
            current.next = ListNode(carry)
        
        # The result is in the next of dummy_head
        return dummy_head.next
