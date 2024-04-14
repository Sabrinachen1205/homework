class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = 0
        a = abs(x)
        while(a != 0):
            temp = a % 10
            num = num * 10 + temp
            a = int(a / 10)  
        if x >= 0 and x == num:
            return True
        else:
            return False