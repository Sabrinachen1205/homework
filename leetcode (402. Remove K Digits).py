class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k==len(num):
            return '0'
        stack=[]
        
        for val in num:
            while k>0 and stack and val<stack[-1]:
                stack.pop()
                k-=1
            stack.append(val)
        
        for i in range(k):
            stack.pop()
        return ''.join(stack).lstrip('0') or '0'