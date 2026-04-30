# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        if (self.isSameTree(root, subRoot)):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot))
        
        


    def isSameTree(self, curr, subRoot):
        if not curr and not subRoot:
            return True
        if curr and subRoot and curr.val == subRoot.val:
            return (self.isSameTree(curr.left, subRoot.left) and self.isSameTree(curr.right, subRoot.right))
        else:
            return False
            
        
        