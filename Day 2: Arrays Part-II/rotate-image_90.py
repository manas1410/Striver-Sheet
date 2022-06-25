'''
problem url :- https://leetcode.com/problems/rotate-image/
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #First trapspose the matrix
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i] =matrix[j][i],matrix[i][j]
                
        #then reverse the each sub list
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
