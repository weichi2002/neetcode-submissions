# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #binary tree condition must satisfy that left < node.val < right
        #in addition to this, they are also bounded by their ancestor
        #for the left side: the upper limit is the parent node value, lower bound is infinity
        #for the right side: the lower limit is the parent node value, upper bound is inifity
        #we will use dfs to explore this relationship 


        def dfs(node, lower, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False

            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
            
        
        return dfs(root, float('-inf'), float("inf"))


