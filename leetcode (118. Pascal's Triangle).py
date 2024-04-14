class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        nums = []
        for i in range(numRows):
            row = []
            for j in range(len(nums)+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(nums[i-1][j-1] + nums[i-1][j])
            nums.append(row)
        return nums