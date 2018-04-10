import collections
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=collections.Counter(list(s))
        print(s)
        s=sorted(s.items(),key=lambda x:x[1],reverse=True)
        print(s)
        res=[]
        for i in s:
            res+=[i[0]]*i[1]
        return ''.join(res)