# Unique Paths
# dp[m][n] = number of paths at location on grid
# initialize dp w/ all 1s, iterate,
# dp[r][c] = dp[r-1][c] + dp[r][c-1]
# time: O(m*n), space: O(m*n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for i in range(m)] # init
        
        for r in range(1, m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
                
        return dp[-1][-1]
