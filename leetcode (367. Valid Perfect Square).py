class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        guess = 1000
        while True:
            p = int(guess)
            q = p + 1
            guess = (guess + num / guess) / 2
            if p*p == num:  # �T�{�O���������
                return True
            if p*p <= num and q*q > num:  # �D��������ơA�]��ڸ�������Ƥ���
                return False