# Kth Smallest Element in a BST
# inorder recursion, store elements in list, return list[k-1]
# time: O(n), space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered_list = []
        def inorder(r):
            if not r:
                return []
            inorder(r.left)
            ordered_list.append(r.val)
            inorder(r.right)
        inorder(root)
        return ordered_list[k-1]
