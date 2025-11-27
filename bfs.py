from collections import deque

# ----------------- Given Code -----------------
class Solution:
    def levelOrder(self, root):
        result = []
        if not root:
            return result
        
        queue = deque([root])
        
        while queue:
            size = len(queue)
            level = []
            
            for _ in range(size):
                node = queue.popleft()
                level.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result

# ----------------------------------------------

# Node Class for Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# -------- YOU ENTER TREE DATA HERE ----------
# Example: tree of [1, 2, 3, 4, 5]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# --------------------------------------------


# Run BFS Level Order
sol = Solution()
print(sol.levelOrder(root))
