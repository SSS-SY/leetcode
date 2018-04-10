class Solution:
    def isPalindrome(self, s, start, end, delCount):
        if delCount > 1:
            return False
        while start < end:
            if s[start] != s[end]:
                break
            start += 1
            end -= 1
        if (start == end) or (start == end+1):
            return True
        return any([self.isPalindrome(s, start+1, end, delCount+1), self.isPalindrome(s, start, end-1, delCount+1)])

    def validPalindrome(self, s):
        return self.isPalindrome(s, 0, len(s)-1, 0)