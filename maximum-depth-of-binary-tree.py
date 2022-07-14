# Max Depth of Binary Tree
# recursion or iterative (w/ deque), traverse tree, +1 current depth
# time: O(N), space: O(logN) if balanced, O(N) worst case

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            return max(l, r) + 1
# iterative
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([])
        if root is not None:
            q.append((1, root))
        depth = 0
        while q:
            this_depth, root = q.popleft()
            if root:
                depth = max(depth, this_depth)
                q.append((this_depth+1, root.left))
                q.append((this_depth+1, root.right))
        return depth
