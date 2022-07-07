# Number of Connected Components in an Undirected Graph
# Union find/Disjoint Set algo: find # of disjoint sets (disregard cycles)
# Find: Determine which subset a particular element is in
# Union: Join two subsets into a single subset (share same edge)
# time: O(edges), space: O(vertices)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        # find subset (root) x belongs to
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # join two subsets
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        # union vertices that share an edge
        for x,y in edges:
            # no need to check for cycle (if parents same in edge)
            union(x,y)
        
        # return number of distinct sets
        roots = [find(i) for i in range(n)]
        return len(set(roots))
