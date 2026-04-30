# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #relationship is left < node.val < right
        #use dfs of some sort, we also know that this is limit is determined by its ancestor. 
        #if we go left, the lower bound is theoretically negative infinite
        #go right, the upperbound is infinite

        def dfs(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        

        return dfs(root, float("-inf"), float("inf"))
            