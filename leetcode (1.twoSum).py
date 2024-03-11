class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        iaAnswer = [] #answer
        ilength = len(nums) #length of nums
        for iIndex1 in range(0, ilength): #loop 1
            for iIndex2 in range(iIndex1+1, ilength): # loop2
                if (nums[iIndex1] + nums[iIndex2]) == target: #two sun
                    iaAnswer.append(iIndex1) #save answer1
                    iaAnswer.append(iIndex2) #save answer2
                    break
        return iaAnswer
        