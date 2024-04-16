class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        s1 = ''
        for x in range(0, len(s)):
            if x == len(s) - 1:
                s1 += s[x][::-1]
            else:
                s1 += s[x][::-1] + ' '
        return s1   