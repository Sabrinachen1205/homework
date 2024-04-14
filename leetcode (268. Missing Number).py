class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_n = len(nums)
        res = len_n
 
        for i in range(len_n):
            res ^= i ^ nums[i]
 
        return res