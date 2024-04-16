class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0

        ans = 0
        prod = 1

        j = 0
        for i, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod /= nums[j]
                j += 1
            ans += i - j + 1

        return ans