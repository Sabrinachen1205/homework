class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, up = 0, len(nums) - 1
        mi = (lo + up) // 2
        while lo <= up:
            if nums[mi] == target: 
                return mi
            elif nums[mi] > target:
                up = mi - 1
            else:
                lo = mi + 1            
            mi = (lo + up) // 2
        return lo
