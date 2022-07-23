# python-algorithms
Python implementations of common algorithms and data structures problems.

# Cheat Sheet
```
def order(root):
    if root:
        print(root.val) # preorder
        order(root.left)
        print(root.val) # in order
        order(root.right)
        print(root.val) # postoreder
```