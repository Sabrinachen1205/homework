class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in s)