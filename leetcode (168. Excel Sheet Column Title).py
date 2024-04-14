class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        dic="ABCDEFGHIJKLMNOPQRSTUVWXYZ"   
        res=[]
        while columnNumber:
            pos=(columnNumber-1)%26
            res.append(dic[pos])
            columnNumber=(columnNumber-1)//26
        res.reverse()
        return "".join(res)