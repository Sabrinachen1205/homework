class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res=0
        for i in range(len(columnTitle)):
            res*=26
            res+=ord(columnTitle[i])-64
        return res