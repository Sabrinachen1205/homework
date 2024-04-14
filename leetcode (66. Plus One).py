class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1]=digits[-1]+1
        
        temp=0
        for i in range(1,len(digits)+1):
            digits[-i]=digits[-i]+temp
            if digits[-i]<10:
                temp=0
                break
            temp=digits[-i]//10
            digits[-i]=digits[-i]%10
            
        if temp != 0:
            digits.insert(0,temp)
        return digits