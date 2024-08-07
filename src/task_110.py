from idlelib.tree import TreeNode
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.balance(root)[1]

    def balance(self, root):
        if root is None:
            return -1, True
        else:
            l_h, l_balanced = self.balance(root.left)
            r_h, r_balanced = self.balance(root.right)

            if l_balanced is True and r_balanced is True:
                if abs(l_h - r_h) < 2:
                    return max(l_h, r_h) + 1, True
        return 1, False
