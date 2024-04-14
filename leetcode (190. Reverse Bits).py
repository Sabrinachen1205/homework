class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res, power = 0, 31
        while n:
            res += (n & 1) << power
            n >>= 1
            power -= 1
        return res