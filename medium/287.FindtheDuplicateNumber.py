import collections
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=collections.Counter(nums)
        for i in nums:
            if nums[i]>1:
                return i