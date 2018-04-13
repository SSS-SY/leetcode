# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sums=0
        self.dfs(root)
        return self.sums
    def dfs(self,root):
        if not root: return 0
        left, right = self.dfs(root.left), self.dfs(root.right)
        self.sums += abs(left - right)
        return root.val + left + right