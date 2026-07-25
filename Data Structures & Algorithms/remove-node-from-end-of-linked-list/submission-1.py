# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next

        
        remove = length - n
        if remove == 0:
            return head.next

        i = 0
        prev, dummy = head, head
        while head:
            if i == remove:
                prev.next = head.next
                head.next = None
                break
            prev = head
            head = head.next
            i += 1
        return dummy