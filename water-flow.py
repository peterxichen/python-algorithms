# (Pacific Atlantic) Water Flow
# create 2 sets of coordinates (reachable to Pacific and reachable to Atlantic), intersection reaches both
# DFS, starting from ocean adjacent coordinates and work backwards
# time: O(r*c), space: O(r*c)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nw_reachable, se_reachable = set(), set()
        # append to "reachable" if adjacent to ocean/ocean-reachable coordinate
        def dfs(r, c, reachable):
            reachable.add((r,c))
            for (r_delta, c_delta) in [(1,0), (0,1), (-1,0), (0,-1)]:
                new_r, new_c = r+r_delta, c+c_delta
                if new_r < 0 or new_r >= len(heights) or new_c < 0 or new_c >= len(heights[0]):
                    continue # skip, out of bounds
                if (new_r, new_c) in reachable:
                    continue # skip, already visited
                if heights[new_r][new_c] < heights[r][c]:
                    continue # skip, shorter (not reachable)
                dfs(new_r, new_c, reachable)
        
        # start from ocean adjacent and work backwords
        for i in range(len(heights)): # row level
            dfs(i, 0, nw_reachable) # left
            dfs(i, len(heights[0])-1, se_reachable) # right
        for i in range(len(heights[0])): # col level
            dfs(0, i, nw_reachable) # top
            dfs(len(heights)-1, i, se_reachable) # bottom

        return list(nw_reachable.intersection(se_reachable))
