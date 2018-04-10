class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=s.split()
        res=res[::-1]
        return ' '.join(res)