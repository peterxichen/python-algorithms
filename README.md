# python-algorithms
Python implementations of common algorithms and data structures problems.

# Cheat Sheet
```
# traversing binarty tree
def order(root):
    if root:
        print(root.val) # preorder
        order(root.left)
        print(root.val) # in order
        order(root.right)
        print(root.val) # postoreder

# Heap/PriorityQueue - BST parent node <= child node (MinHeap)

import heapq # for MaxHeap multiply by -1
heapq.heapify(H) # convert list to heap (actually `O(N))
heapq.heappush(H,8) # adds to heap ~O(logN)
heapq.heappop(H) # returns smallest ~O(1)
heapq.heapreplace(H,6) # replcae smallest w/ value
heapq.nlargest/nsmallest(n, iter, key=None)
```