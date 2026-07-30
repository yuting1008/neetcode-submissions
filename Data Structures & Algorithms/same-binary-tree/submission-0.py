# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_list = []
        q_list = []

        def dfs(lst, curr):
            if not curr:
                lst.append([None, None])
                return 0
            left = dfs(lst, curr.left)
            right = dfs(lst, curr.right)
            height = 1 + max(left, right)
            lst.append([curr.val, height])
            return height

        dfs(p_list, p)
        dfs(q_list, q)
        return p_list == q_list
        