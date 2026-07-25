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
        # res = dummy = head
        # for i in range(1, mid):
        #     nxt = dummy.next
        #     if i % 2 != 0 and reverse:
        #         dummy.next = reverse
        #         reverse = reverse.next
        #     dummy = nxt
        # return res

'''
res = dummy = head
head = head.next

[0, 1, 2] head
    h 

[6, 5, 4, 3] reverse
 r

[0] dummy


i = 1 (i % 2 != 0),

[0, 1, 2, 3, 4, 5, 6] head
    h 

[6, 5, 4, 3, 2, 1, 0] reverse
    r

[0, 6] dummy

i = 2 (i % 2 == 0),

[0, 1, 2, 3, 4, 5, 6] head
       h 

[6, 5, 4, 3, 2, 1, 0] reverse
    r

[0, 6, 1] dummy
'''
