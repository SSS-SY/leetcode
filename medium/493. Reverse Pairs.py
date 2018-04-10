import collections
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res,i=0,len(nums)-1
        while i>0:
        	temp=collections.Counter(nums[:i])
        	print(temp,nums[:i])
        	print(2*nums[i]+1,max(nums[:i]))
        	for j in range(2*nums[i]+1,max(nums[:i])+1):
        		print(j)
        		if j in temp:
        			res+=temp[j]
        	i-=1
        return res
print(Solution().reversePairs([2147483647,2147483647,-2147483647,-2147483647,-2147483647,2147483647]))