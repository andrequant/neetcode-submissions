# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.check(root) == -1:
            return False
        else:
            return True
    
    def check(self, node):

        if not node:
            return 0

        left = self.check(node.left)
        if left == -1:
            return -1
        
        right = self.check(node.right)
        if right == -1:
            return -1

        if abs(right-left) > 1:
            return -1
        
        return 1 + max(left, right)


