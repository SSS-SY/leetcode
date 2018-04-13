# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rows,level=[],[root]
    	while root and level:
        	rows.append([node.val for node in level])            
        	level = [kid for n in level for kid in (n.left, n.right) if kid]
    	return [max(i) for i in rows]