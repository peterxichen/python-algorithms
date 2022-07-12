# Rotate Matrix/Image (90 degrees clockwise)
# transpose (reverse on diagonal) + reflect (reverse left to right) w/ helper methods
# time: O(M), space: O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(m): # across y=-x
            for i in range(len(m)):
                for j in range(i+1, len(m)): # iter for below y=-x
                    m[i][j], m[j][i] = m[j][i], m[i][j]
        def reflect(m): # across y axis
            # i stays constant, flip j index
            for i in range(len(m)):
                for j in range(len(m)//2): # iter left half
                    m[i][j], m[i][-j-1] = m[i][-j-1], m[i][j]
        transpose(matrix)
        reflect(matrix)
