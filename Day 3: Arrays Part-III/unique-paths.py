'''
problem url:- https://leetcode.com/problems/unique-paths
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        nn = m+n-2
        r = m-1
        res = 1 
        for i in range(1,r+1):
            res= res*(nn-r+i)/(i)
        return int(res)
                
