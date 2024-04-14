# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        ans = [False]
        
        def tree_traversal(root, curr_sum,ans):
            curr_sum += root.val
    
            if root.left is None and root.right is None:
                if curr_sum == targetSum:
                    ans[0]=True 
                    
            if root.left:
                tree_traversal(root.left, curr_sum,ans)
            
            if root.right:
                tree_traversal(root.right, curr_sum,ans)
        
        if root:
            tree_traversal(root, 0,ans)
        return ans[0]