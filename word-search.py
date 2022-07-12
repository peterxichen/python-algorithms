# Word Search
# helper method for DFS in 4 directions, traverse each element in matrix and run DFS
# time: O(N*3^L), space: O(L) from recur in stack
# where N is num cells, L is word len

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, substr, r, c):
            if len(substr) == 0:
                return True # bottom case
            if (r<0 or c<0 or r>=len(board) or c>=len(board[0]) or board[r][c]!=substr[0]):
                # out of bounds OR first index does not match -> state invalid
                return False
            
            word_found = False
            board[r][c] = '#' # mark as visited
            for dirs in [(1,0), (-1,0), (0,1), (0,-1)]:
                word_found = dfs(board, substr[1:], r+dirs[0], c+dirs[1])
                if word_found:
                    break
            board[r][c] = substr[0] # revert original state (un-visit)
            return word_found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j):
                    # can first check if 1st letter
                    # if board[i][j] == word[0]
                    return True
        return False
