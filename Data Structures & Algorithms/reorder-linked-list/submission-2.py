# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev, curr = None, second
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        p1, p2 = head, prev
        while p2:
            n1, n2 = p1.next, p2.next
            p1.next = p2
            p2.next = n1
            p1 = n1
            p2 = n2
        return p2

'''
[0, 1, 2, 3]
[6, 5, 4]

node0 -> node6
node6 -> node1

node1 -> node5
node5 -> node2

node2 -> node4
node4 -> node3
'''