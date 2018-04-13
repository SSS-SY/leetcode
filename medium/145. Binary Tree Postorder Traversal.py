# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res=[]
        self.postSearch(root)
        return self.res
    def postSearch(self,root):
        if root:
            self.postSearch(root.left)
            self.postSearch(root.right)
            self.res.append(root.val)