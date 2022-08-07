# Word Search II (return all words on board)
# build trie of vocabulary, helper method to traverse grid recursively in 4 directions,
# search in trie and mark as visited for current recursion, do for each value in grid
# time: O(board size*constant^max len(word)), space: O(words) for trie size

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie of vocabulary
        trie = {}
        for w in words:
            cur = trie
            for c in w:
                if not cur.get(c):
                    cur[c] = {}
                cur = cur[c]
            cur['END'] = w # mark end

        matches = [] # store results
        
        # helper method to traverse grid
        def backtrack(r, c, parent):
            char = board[r][c]
            cur = parent[char]
            match = cur.get('END', None)
            if match:
                matches.append(match)
                del cur['END'] # to avoid duplicates (or use set)

            board[r][c] = '#' # mark as visited for current recursion
            for direction in [(-1,0), (0,1), (1,0), (0,-1)]:
                rr, cc = r+direction[0], c+direction[1]
                # not out of bounds
                if rr>=0 and rr<len(board) and cc>=0 and cc<len(board[0]):
                    # if character in current trie node
                    if board[rr][cc] in cur:
                        backtrack(rr, cc, cur)
            board[r][c] = char # restore
            
            if not cur: del parent[char] # optional optimization
        
        # traverse grid
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in trie:
                    backtrack(r,c,trie)
        return matches
