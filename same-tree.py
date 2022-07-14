# Same Tree
# recursion or iterative (w/ deque), traverse tree
# check if both null, only one null, then values
# time: O(N), space: O(logN) if balanced O(N) worst case

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not q or not p:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# iterative
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p,q):
            if not p and not q:
                return True
            elif not q or not p:
                return False
            elif p.val != q.val:
                return False
            return True

        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            if p: # q not needed
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return True
