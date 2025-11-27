from collections import defaultdict, deque
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional['TreeNode']) -> List[List[int]]:
        if not root:
            return []
        d = defaultdict(lambda: defaultdict(list))
        q = deque([(root, 0, 0)])  # node, vertical, level
        
        while q:
            node, vertical, level = q.popleft()
            d[vertical][level].append(node.val)
            
            if node.left:
                q.append((node.left, vertical-1, level+1))
            if node.right:
                q.append((node.right, vertical+1, level+1))
        
        ans = []
        for vertical in sorted(d.keys()):
            col = []
            for level in sorted(d[vertical].keys()):
                col.extend(sorted(d[vertical][level]))
            ans.append(col)
        
        return ans
def build_tree(arr):
    if not arr:
        return None
    nodes = [TreeNode(x) if x is not None else None for x in arr]
    for i in range(len(arr)):
        if nodes[i]:
            left_index = 2*i + 1
            right_index = 2*i + 2
            if left_index < len(arr):
                nodes[i].left = nodes[left_index]
            if right_index < len(arr):
                nodes[i].right = nodes[right_index]
    return nodes[0]
arr = [1, 2, 3, 4, 5, 6, 7]

root = build_tree(arr)
sol = Solution()
output = sol.verticalTraversal(root)
print("Vertical Order Traversal:", output)
