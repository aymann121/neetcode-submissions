# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [(root,0)]
        res = []
        while queue:
            node = queue.pop()
            if not node[0]: continue
            if len(res) < node[1] +1:
                res.append([node[0].val])
            else:
                res[node[1]].append(node[0].val)

            queue.append((node[0].right, node[1]+1))
            queue.append((node[0].left, node[1]+1))
        return res
