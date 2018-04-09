class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res,dic=[],{}
        for i in strs:
            ch=''.join(sorted(i))
            if ch not in dic:
                dic[ch]=[i]
            else: dic[ch].append(i)
        return list(dic.values())