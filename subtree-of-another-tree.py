# Subtree of Another Tree
# helper method implement isSameTree, traverse root tree and check against subroot tree
# time: O(N*M) S~O(logN), where N num nodes in root M subroot

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # helper method check if same tree
        def isSameTree(p, q): # time: O(N), space: O(logN)
            if not p and not q:
                return True
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            else:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if not subRoot:
            return True
        elif not root:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
