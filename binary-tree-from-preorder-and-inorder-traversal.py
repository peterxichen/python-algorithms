# Construct Binary Tree from Preorder and Inorder Traversal
# init global variables: preorder index (=0) + hashmap strong "inorder" (k: value, v: index),
# helper method for recursion, start with root in "preorder", look for root in "inorder",
# left/right of root in "inorder" are the left/right subtrees, increment preorder index for next node
# time: O(n), space: O(n) (map + recur implicit stack)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root -> left -> right
        # inorder: left -> root -> right
        # preorder[0] is root, look for root in inorder array (left/right are subtrees)
        
                
        preorder_index = 0 # global tracking
        inorder_d = {} # hashmap to store "inorder" index (k: value, v: index) 
        for i, val in enumerate(inorder):
            inorder_d[val] = i

        def recurInorder(l, r):
            nonlocal preorder_index
            if l > r:
                return None # no elements
            this_val = preorder[preorder_index]
            this_node = TreeNode(this_val)
            preorder_index += 1
            # recur left/right ranges of "inorder" of subtree
            this_node.left = recurInorder(l, inorder_d[this_val]-1) # left subtree
            this_node.right = recurInorder(inorder_d[this_val]+1, r) # right subtree
            return this_node
        
        return recurInorder(0, len(preorder)-1)
