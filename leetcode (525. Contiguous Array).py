class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic=defaultdict(int)
        dic[0]=-1
        res=0
        count=0
        for pos,val in enumerate(nums):
            count+=1 if val==1 else -1
            if count in dic:
                res=max(res,pos-dic[count])
            else:
                dic[count]=pos
        return res
