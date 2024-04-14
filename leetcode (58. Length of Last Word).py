class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        sA = s.strip()
        sS = sA.split(' ')
        return len(sS[len(sS)-1])