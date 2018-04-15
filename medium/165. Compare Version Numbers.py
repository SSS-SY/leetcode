class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1=(version1.split('.'))
        version2=(version2.split('.'))
        i,maxlen,minlen=0,max(len(version1),len(version2)),min(len(version1),len(version2))
        while i<minlen:
            i1,i2=int(version1[i]),int(version2[i])
            if i1<i2:
                return -1
            if i1>i2:
                return 1
            i+=1
        if len(version1)>len(version2):
            while i<maxlen:
                if int(version1[i])!=0:
                    return 1
                i+=1
        elif len(version1)<len(version2):
            while i<maxlen:
                if int(version2[i])!=0:
                    return -1
                i+=1
        return 0

print(Solution().compareVersion("1","1.1"))