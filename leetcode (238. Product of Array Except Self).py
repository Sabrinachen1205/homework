class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l2r = [1 for _ in range(n)]
        r2l = [1 for _ in range(n)]

        cur_val = 1
        for i in range(n):
            cur_val *= nums[i]
            l2r[i] = cur_val

        cur_val = 1
        for i in range(n-1, -1, -1):
            cur_val *= nums[i]
            r2l[i] = cur_val

        result = [1 for _ in range(n)]
        for i in range(n):
            if i == 0:
                result[i] = r2l[i+1]
            elif i == n-1:
                result[i] = l2r[i-1]
            else:
                result[i] = l2r[i-1] * r2l[i+1]
        return result