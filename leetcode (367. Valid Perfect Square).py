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
            if p*p == num:  # 確認是完全平方數
                return True
            if p*p <= num and q*q > num:  # 非完全平方數，因其根號介於兩整數之間
                return False