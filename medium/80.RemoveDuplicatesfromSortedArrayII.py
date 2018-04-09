import collections
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=collections.Counter(nums)
        res2=list(res.keys())
        res2.sort()
        res3=[]
        for num in res2:
        	res3.append(num) 
        	if res[num]>1:
        		res3.append(num)
        for i in range(len(res3)):
        	nums[i]=res3[i]
        return len(res3)