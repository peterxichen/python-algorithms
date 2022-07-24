# Longest Common Subsequence
# dp grid of text1 * text2, initialize all 0s, traverse in reverse,
# dp[i][j] is longest common subsequence of text1[i:] and text2[j:],
# if corresponding letters for a cell are same then +1, build dp to (0,0)
# time: O(len text1*len text2), space: O(len text1*len text2)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # make grid of 0s (text1+1 rows * text2+1 cols)
        dp_grid = [[0]* (len(text2)+1) for x in range(len(text1)+1)]
        
        # iterate in reverse
        for c in reversed(range(len(text2))):
            for r in reversed(range(len(text1))):
                # if corresponding characters for this cell are same
                if text2[c] == text1[r]:
                    dp_grid[r][c] = 1 + dp_grid[r+1][c+1]
                else:
                    dp_grid[r][c] = max(dp_grid[r+1][c], dp_grid[r][c+1])
        # original problem at (0,0)
        return dp_grid[0][0]
