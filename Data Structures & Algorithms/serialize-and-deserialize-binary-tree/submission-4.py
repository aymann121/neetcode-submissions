# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #do a bfs and turn the tree into an array
        treeArr = []
        queue = deque([root])
        while queue:
            e = queue.popleft()
            if e:
                treeArr.append(str(e.val))
                queue.append(e.left)
                queue.append(e.right)
            else: treeArr.append('null')
        return '-'.join(treeArr)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split('-')
        if not vals or vals[0] == 'null': return None
        queue = deque([TreeNode(int(vals[0]), None, None)])
        i = 0
        head = queue[0]
        while queue:
            node = queue.popleft()
            if i+1 < len(vals):
                if vals[i+1] != 'null':
                    node.left = TreeNode(int(vals[i+1]), None, None)
                    queue.append(node.left)
                i += 1
            if i+1 < len(vals):
                if vals[i+1] != 'null':
                    node.right = TreeNode(int(vals[i+1]), None, None)
                    queue.append(node.right)
                i += 1
        
        return head



