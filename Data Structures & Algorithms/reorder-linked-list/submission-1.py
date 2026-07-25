# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0 # length
        dummy = head
        while dummy:
            n += 1
            dummy = dummy.next
        
        mid = (n + 1) // 2
        reverse, curr = None, head
        for i in range(n):
            temp = curr.next
            if i >= mid:
                curr.next = reverse
                reverse = curr
            if i == mid - 1:
                curr.next = None
            curr = temp

        p1, p2 = head, reverse
        while p2:
            n1, n2 = p1.next, p2.next
            p1.next = p2
            p2.next = n1
            p1 = n1
            p2 = n2
        return p2