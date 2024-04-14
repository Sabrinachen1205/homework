class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=""
        for i in range(len(strs[0])):
            for j in strs:
                if i >len(j)-1:
                    return ans
                if strs[0][i]!=j[i]:
                    return ans
            ans=ans+strs[0][i]
        return ans