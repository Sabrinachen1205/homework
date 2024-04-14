class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1=num1[::-1]
        num2=num2[::-1]
        
        if len(num1)>len(num2):
            num2=num2+"0"*(len(num1)-len(num2))
        else:
            num1=num1+"0"*(len(num2)-len(num1))
            
        ans=""
        temp=0    
        for i in range(len(num1)):
            x=int(num1[i])+int(num2[i])+temp
            temp=x//10
            ans=str(x%10)+ans
            
        if temp:
            ans=str(temp)+ans
            
        return ans
