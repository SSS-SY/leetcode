import collections
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=collections.Counter(nums)
        res=list(res.keys())
        for i in range(len(res)):
            nums[i]=res[i]
        return len(res)