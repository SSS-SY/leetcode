class Solution:
    def twoSum(self, nums, target):
        dic={}
        for n in range(len(nums)):
            if target-nums[n] in dic:
                return [dic[target-nums[n]],n]
            if nums[n] not in dic:
                dic[nums[n]]=n