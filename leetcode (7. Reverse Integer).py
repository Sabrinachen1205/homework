class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = [1,-1][x<0]
        rev, x = 0, abs(x)
        while x:
            x, mod = divmod(x, 10)
            rev = rev*10 + mod
        return sign*rev if -pow(2,31) <= sign*rev <= pow(2,31)-1 else 0