# Graph Valid Tree (contains no cycles)
# Union find/Disjoint Set algo: used to check whether an undirected graph contains cycle
# Find: Determine which subset a particular element is in
# Union: Join two subsets into a single subset (share same edge).
# time: O(n), space: O(n)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # each node must be connected w/ no repeats
        if n-1 != len(edges):
            return False
        
        # each vertex belongs to itself's set
        parent = {i: i for i in range(n)}
        
        # FIND: traces parent until finds root
        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]
        
        # UNION: find roots for A and B then sets B's parent to be A
        for e in edges:
            set1, set2 = find(e[0]), find(e[1])
            if set1 == set2: # cycle is found (same parent)
                return False
            parent[set1] = set2 # UNION edged vertices
        return True
