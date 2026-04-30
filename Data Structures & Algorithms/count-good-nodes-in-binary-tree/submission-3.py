# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #preorder traversal: root, left, right
        #keep track of parents max


        def dfs(node, maxParentVal):
            if not node:
                return 0
            res = 1 if node.val >= maxParentVal else 0
            maxParentVal = max(node.val, maxParentVal)
            res += dfs(node.left, maxParentVal)
            res += dfs(node.right, maxParentVal)
            return res

        return dfs(root, root.val)

            
