# Validate Binary Search Tree (Valid BST)
# inorder traversal, check each incremental node is larger
# time: O(n), space: O(n) due to function call overhead

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        compare = float('-inf') # store previous node value
        # left -> node -> right
        def inorder(root):
            nonlocal compare
            if not root:
                return True
            if not inorder(root.left):
                return False # continue if true
            if root.val <= compare:
                return False
            compare = root.val
            return inorder(root.right)
        return inorder(root)
