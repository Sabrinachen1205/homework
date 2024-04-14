class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        checkNumber = 0
        if nums:
            for i in range(len(nums)):
                if(checkNumber != nums[i] or i == 0):
                    checkNumber = nums[i]
                    nums[answer] = checkNumber
                    answer += 1
        return answer