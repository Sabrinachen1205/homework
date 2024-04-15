# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        s = ''
        def dfs(root, s):
            if not root.left and not root.right:
                self.res += int(s+str(root.val))
            if root.left:
                dfs(root.left, s+str(root.val))
            if root.right:
                dfs(root.right, s+str(root.val))
        dfs(root, s)
        return self.res
