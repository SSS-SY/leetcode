# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        self.presearch(root,res)
        return res
    def presearch(self,root,res):
        if root:
            res.append(root.val)
            self.presearch(root.left,res)
            self.presearch(root.right,res)