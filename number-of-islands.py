# Number of Islands
# DFS or BFS, # of islands = # of root nodes
# time: O(rows*cols), space: O(r*c)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return None
        # of islands = # of root nodes
        def dfs(grid, r, c):
            if (r<0 or c<0 or r>= len(grid) or c>=len(grid[0]) or grid[r][c]=='0'):
                return
            grid[r][c] = '0' # mark as "seen"
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
            dfs(grid, r, c+1)
        num = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1': # "root"
                    num += 1
                    dfs(grid, r, c)
        return num
# BFS (space: O(min(r, c)))
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        num = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    num+=1
                    grid[r][c] = '0' # visited
                    neighbors = deque([r*len(grid[0])+c]) # store coordinates as integer
                    while neighbors: # bfs to mark visitors
                        temp = neighbors.popleft()
                        rr, cc = temp//len(grid[0]), temp%len(grid[0])
                        
                        if rr-1 >= 0 and grid[rr-1][cc] == '1':
                            neighbors.append((rr-1)*len(grid[0])+cc)
                            grid[rr-1][cc] = '0' # mark visited
                        if (rr+1 <len(grid) and grid[rr+1][cc]=='1'):
                            neighbors.append((rr+1)*len(grid[0])+cc)
                            grid[rr+1][cc] = '0'
                        if (cc-1>=0 and grid[rr][cc-1] == '1'):
                            neighbors.append(rr*len(grid[0]+cc-1))
                            grid[rr][cc-1] = '0'
                        if (cc+1<len(grid[0]) and grid[rr][cc+1]=='1'):
                            neighbors.append(rr*len(grid[0])+cc+1)
                            grid[rr][cc+1] = '0'
        return num
