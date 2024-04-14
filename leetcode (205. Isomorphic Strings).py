class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = dict()
        n = dict()
        for i, c in enumerate(s):
            if c in m and m[c] != t[i]:
                return False
            if t[i] in n and c != n[t[i]]:
                return False
            m[c] = t[i]
            n[t[i]] = c
        return True