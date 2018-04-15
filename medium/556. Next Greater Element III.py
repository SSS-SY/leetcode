class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums=list(str(n))
        i=len(nums)-1
        while i>0:
            if nums[i-1]<nums[i]:
                break
            i-=1
        if i==0:
            print(2)
            return -1
        index,x=i,nums[i-1]
        for j in range(i+1,len(nums)):
            if (nums[j]>x and nums[j]<=nums[index]):
                index=j
        print(i,index)
        nums[index],nums[i-1]=nums[i-1],nums[index]
        temp=sorted(nums[i:])
        nums=nums[:i]+temp
        nums=int(''.join(nums))
        return nums if nums<2**31 else -1