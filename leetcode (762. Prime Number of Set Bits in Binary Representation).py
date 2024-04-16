class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        prime_nums = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        
        def count_1bits(n):
            ans = 0
            while n:
                ans += 1
                n = n & (n-1)
            return ans
        
        ans = 0
        for n in range(left, right+1):
            bits = count_1bits(n)
            if bits in prime_nums:
                ans += 1
        return ans