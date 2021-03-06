# Binary Tree Level Order Traversal
# scan level by level, traverse w/ recursion
# helper method takes root and level value as args
# time: O(N), space: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] # tracks result
        if not root:
            return res
        
        def traverse(node, level):
            # initialize if first time reaching level
            if len(res) == level:
                res.append([])
            # append current value
            res[level].append(node.val)
            if node.left:
                traverse(node.left, level+1)
            if node.right:
                traverse(node.right, level+1)
        
        traverse(root, 0)
        return res
