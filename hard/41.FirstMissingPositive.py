class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        i=0
        while i<n:
            if nums[i]!=(i+1) and nums[i]>=1 and nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            else:
                i+=1
        for i in range(n):
            if (nums[i]!=(i+1)):
                return i+1
        return n+1