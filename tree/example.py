from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def dfs_recursive(self, root: Optional['TreeNode']):
        if not root:
            return # Base case: we hit a dead end (null node)
            
        print(root.val)          # 1. Process the current node
        self.dfs_recursive(root.left)  # 2. Recursively explore the whole left side
        self.dfs_recursive(root.right) # 3. Recursively explore the whole right side


    def bfs_iterative(self, root: Optional['TreeNode']):
        if not root:
            return
            
        queue = deque([root]) # Initialize queue with the root node
        
        while queue:
            # Take the node out from the front of the queue
            curr = queue.popleft()
            print(curr.val) # Process it
            
            # Add its children to the back of the queue to be processed later
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

# dfs -> stack
# bfs -> queue

# Creating a small tree:
#     1
#    / \
#   2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Level 0 (Root)
root = TreeNode(1)

# Level 1 (Children of 1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Level 2 (Children of 2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Level 2 (Children of 3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("DFS traversal:")
root.dfs_recursive(root) # Outputs: 1, 2, 3

print("BFS traversal:")
root.bfs_iterative(root) # Outputs: 1, 2, 3