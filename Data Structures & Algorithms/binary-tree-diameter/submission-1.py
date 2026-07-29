# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def depth(node):
            nonlocal res
            if not node:
                return 0
            ld = depth(node.left)
            rd = depth(node.right)
            res = max(res, ld + rd)
            return max(ld, rd) + 1
        depth(root)
        return res


