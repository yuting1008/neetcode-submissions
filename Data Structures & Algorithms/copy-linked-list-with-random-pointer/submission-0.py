"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            copies[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = copies[cur]
            copy.next = copies[cur.next]
            copy.random = copies[cur.random]
            cur = cur.next
        
        return copies[head]
