# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        ids = {inorder[i]:i for i in range(len(inorder))}

        def helper(preorder, inorder):
            if not preorder: return None
            val = preorder[0]
            inorderid = inorder.index(val)
            res = TreeNode(val, None, None)

            res.left = helper(preorder[1:inorderid+1], inorder[0:inorderid])
            res.right = helper(preorder[inorderid+1:], inorder[inorderid+1:])
            return res

        return helper(preorder,inorder)
