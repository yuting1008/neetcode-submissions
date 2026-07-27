# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(0)
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            val = total % 10
            node = ListNode(val)
            curr.next = node
            curr = curr.next
            carry = (total - val) // 10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = l1.val + carry
            val = total % 10
            node = ListNode(val)
            curr.next = node
            curr = curr.next
            carry = (total - val) // 10
            l1 = l1.next
        
        while l2:
            total = l2.val + carry
            val = total % 10
            node = ListNode(val)
            curr.next = node
            curr = curr.next
            carry = (total - val) // 10
            l2 = l2.next

        if carry != 0:
            node = ListNode(carry)
            curr.next = node
        
        return dummy.next