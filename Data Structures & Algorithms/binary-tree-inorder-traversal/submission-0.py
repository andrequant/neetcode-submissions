# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        lis = []
        
        if not root:
            return lis

        if root.left:
            lis.extend(self.inorderTraversal(root.left))
        
        lis.append(root.val)

        if root.right:
            lis.extend(self.inorderTraversal(root.right))

        return lis



        