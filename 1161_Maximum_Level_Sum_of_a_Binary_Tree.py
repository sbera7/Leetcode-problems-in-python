# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        temp_q = deque([root])
        max_sum = root.val
        level, max_level = 1, 1
        while q:
            level_sum = 0
            next_level = []

            for node in q:
                level_sum += node.val    
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            q = next_level
            level += 1
        return max_level 
