# Clone Graph
# DFS or BFS
# time: O(V+E), space: O(V)

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node, visited):
            if not node:
                return
            if node in visited: # handle visited nodes
                return visited[node]
            visited[node] = Node(node.val, []) # create clone
            if node.neighbors: # create neighboring nodes
                for neighbor in node.neighbors:
                    visited[node].neighbors.append(dfs(neighbor, visited))
            return visited[node]
        # {} tracks visited nodes to avoid cycle
        # k: original node, v: cloned node
        return dfs(node, {})

# BFS
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        visited = {} # {} tracks visited nodes to avoid cycle
        # k: original node, v: cloned node
        queue = deque([node]) # add root to queue
        visited[node] = Node(node.val, []) # clone root
        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor]) # add neighbor to clone
        return visited[node] # root 
