class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        word=list(word)
        total=0;
        for i in range(65,91):
            total+=word.count(chr(i))
        return True if total==0 or total==len(word) or total==1 and word[0]>='A' and word[0]<='Z' else False