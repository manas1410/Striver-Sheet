'''
problem url:- https://leetcode.com/problems/majority-element-ii/
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = len(nums)//3
        d = {}
        for i in nums:
            try:
                d[i]+=1
            except:
                d[i]=1
        l = []
        for i in d.keys():
            if d[i]>majority:
                l.append(i)
        return l
