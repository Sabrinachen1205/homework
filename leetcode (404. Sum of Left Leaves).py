# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # edge case
        if root == None:
            return 0
        
        # regular case
        stack = [(root, False)]
        result = 0
        while len(stack) != 0:
            root, is_left = stack.pop()
            if root.left == None and root.right == None and is_left:
                result = result + root.val
            if root.left != None:
                stack.append((root.left, True))
            if root.right != None:
                stack.append((root.right, False))
        return result