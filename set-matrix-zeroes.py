# Set Matrix Zeroes
# use first element of each row + col as flag indicator
# traverse matrix and flip based on first element
# time: O(r*c), space: O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # use first cell of each row, col as indicator
        first_col = False # handle if 1st col contains 0
        first_row = False # handle if 1st row contains 0
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row = True
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col = True
            for j in range(1, len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # use indicator to flip zeroes
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    # if first element is zero
                    matrix[i][j]=0
        
        # if matrix[0][0]==0 will suffice, no need to check both 1st row + col
        # handle first row
        if first_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        # handle first column
        if first_col:
            for i in range(len(matrix)):
                matrix[i][0]=0
