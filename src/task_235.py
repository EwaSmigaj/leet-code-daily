# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        common = root
        while(True):
            if common.val > p.val and common.val > q.val:
                common = common.left
            elif common.val < p.val and common.val < q.val:
                common = common.right
            else:
                return common

