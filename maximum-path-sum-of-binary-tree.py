# Binary Tree Maximum Path Sum
# greedy, helper method to traverse tree,
# calculate max contribution of node plus either left or right path
# time: O(N), space: O(tree height e.g. logN or N at worst)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf') # track answer
        
        # helper method to traverse tree
        # calculates max contribution of node + left OR right path
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            # max sum on sub trees (ignore if neg)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # track max_sum w/ current node as "root"
            max_sum = max(node.val + left_gain + right_gain, max_sum)

            return node.val + max(left_gain, right_gain)
        max_gain(root)
        return max_sum
