class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        flag = True
        if num<0:
            flag = False
            num = -num
        r = ''
        while num>0:
            m = num % 7
            r = str(m)+r
            num = num//7
        if not flag :
            r = '-' + r
        return r