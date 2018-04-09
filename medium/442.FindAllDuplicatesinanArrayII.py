import collections
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        nums=collections.Counter(nums)
        for g,v in nums.items():
            if v>1:
                res.append(g)
        return res