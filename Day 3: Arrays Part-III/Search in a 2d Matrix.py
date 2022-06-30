'''
problem url:- https://leetcode.com/problems/search-a-2d-matrix/
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans = False
        for i in range(len(matrix)):
            if (target>=matrix[i][0] and target<=matrix[i][(len(matrix[i]))-1]):
                start,last=0,len(matrix[i])-1
                mid=(start+last)//2
                while(start<=last):
                    #print(mid)
                    if(matrix[i][mid]==target):
                        ans=True
                        break
                    elif matrix[i][mid]> target:
                        last = mid - 1
                        
                    else:
                        start = mid+1
                    mid = (last+start)//2
                        
                if ans == True:
                    break
        return ans
