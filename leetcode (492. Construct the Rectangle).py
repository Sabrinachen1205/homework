class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        x=int(sqrt(area))
        
        while True:
            if area%x==0:
                return [area//x,x]
            else:
                x=x-1