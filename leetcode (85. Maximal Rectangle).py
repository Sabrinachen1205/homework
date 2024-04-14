class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #每層都更新res,並累加高度
        if not matrix:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        heights=[0]*n
        res=0
        for row in matrix:
            for j in range(n):
                if row[j]=='1':
                    heights[j]+=1
                else:
                    heights[j]=0
            res=max(res,self.maxArea(heights))
        return res
    
    def maxArea(self,heights):
        if not heights:
            return 0
        stack=[]
        Area=0
        heights.append(0)
        for pos in range(len(heights)):
            if not stack or heights[stack[-1]]<heights[pos]:
                stack.append(pos)
            else:
                while stack and heights[stack[-1]]>=heights[pos]:
                    curH=heights[stack[-1]]
                    stack.pop()
                    curW= pos if not stack else pos-stack[-1]-1
                    Area=max(Area,curH*curW)
                stack.append(pos)
        return Area
    
