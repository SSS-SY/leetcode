import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        self.res=list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.res=list(self.nums)     
        return self.res

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.res)
        return self.res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()