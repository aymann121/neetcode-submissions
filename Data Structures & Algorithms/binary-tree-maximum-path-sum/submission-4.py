# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    memo = {}
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxSinglePath(node):
            if not node: return 0
            if node in self.memo: return self.memo[node]
            self.memo[node] = max(node.val, maxSinglePath(node.left)+ node.val, maxSinglePath(node.right)+ node.val)
            return self.memo[node]
        
        if not root: return float('-infinity')
        left = max(maxSinglePath(root.left), 0)
        right = max(maxSinglePath(root.right),0)

        return max(self.maxPathSum(root.left), self.maxPathSum(root.right), left + right + root.val)
