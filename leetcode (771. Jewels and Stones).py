class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        iSum = 0
        lStones = list(stones)
        for i in range(0,len(jewels),1):
            iSum += lStones.count(jewels[i])
        return iSum