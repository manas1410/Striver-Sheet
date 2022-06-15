'''
problem url :- https://leetcode.com/problems/set-matrix-zeroes/
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cols = 1
        row_size = len(matrix)
        col_size = len(matrix[0])
        
        for i in range(row_size):
            if matrix[i][0] == 0: 
                cols = 0
            for j in range(1,col_size):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(row_size-1,-1,-1):
            for j in range(col_size-1,0,-1):
                if matrix[i][0] == 0 or matrix[0][j]==0:
                    matrix[i][j] = 0
            if cols == 0: 
                matrix[i][0] = 0
