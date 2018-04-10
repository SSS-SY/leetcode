# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        self.search(root,res)
        return res
    def search(self,root,res):
        if root:
            self.search(root.left,res)
            res.append(root.val)
            self.search(root.right,res)