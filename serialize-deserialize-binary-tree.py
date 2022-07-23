# Serialize and Deserialize Binary Tree
# use DFS, serialize by recrusion traverse, split with '#'
# deserialize by splitting data by '#', traverse to build tree, pop(0) at each step
# time/space for both operations: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def traverse(root, s):
            if root is None:
                s += 'END#'
            else:
                s += str(root.val) + '#'
                s = traverse(root.left, s)
                s = traverse(root.right, s)
            return s
        return traverse(root, '')

    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # must pop, l[1:] won't modify original object
        def traverse(l):
            if l[0] == 'END':
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = traverse(l)
            root.right = traverse(l)
            return root
        return traverse(data.split('#'))
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
