class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result=''
        for i in s:
            if i.isalnum():
                result+=i.lower()
        if result==result[::-1]:
            return True
        return False