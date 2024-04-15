class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1: return True
        if not word[0].isupper() and word[1].isupper(): return False
        
        for i in range(1, len(word)-1):
            if word[i].isupper() != word[i+1].isupper(): return False
        
        return True