'''
problem url:- https://leetcode.com/problems/powx-n/
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
        '''if n<0:
            return self.myPow(1/x,-1*n)
        if n==1:
            return x
        if n>1 and n%2==0:
            num = self.myPow(x,n//2)
            return num * num
        return x*self.myPow(x,n-1)'''
