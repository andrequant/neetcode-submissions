# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.q = deque()

        self.getQueue(root, k)

        return self.q[k-1]

    
    def getQueue(self, root, k):

        if len(self.q) == k:
            return

        if root.left:
            self.getQueue(root.left, k)
        
        self.q.append(root.val)

        if root.right:
            self.getQueue(root.right, k)

