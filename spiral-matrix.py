# Spiral Matrix
# tracks starting index for each direction (x4), traverse in spiral
# time: O(r*c), space: O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(matrix), len(matrix[0]) # store lengths
        up, left, right, down = 0,0,cols-1,rows-1 # starting index
        
        while len(res) < rows*cols:
            # left to right
            for c in range(left, right+1):
                res.append(matrix[up][c])
            # top to bottom
            for r in range(up+1, down+1):
                res.append(matrix[r][right])
            # right to left
            if up != down: # check if different row
                for c in range(right-1, left-1, -1):
                    res.append(matrix[down][c])
            # bottom to up
            if left != right: # check if different col
                for r in range(down-1, up, -1):
                    res.append(matrix[r][left])
            left += 1
            right -= 1
            up += 1
            down -= 1
        return res
