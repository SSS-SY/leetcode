class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[0]
        for i in range(n):
            j=2**i
            temp=len(res)-1
            while temp>=0:
                res.append(res[temp]+j)
                temp-=1
        return res