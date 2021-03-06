class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
    		
print(Solution().subsets([1,2,3]))