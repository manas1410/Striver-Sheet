'''
problem url :-https://leetcode.com/problems/majority-element/
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)//2
        d = {}
        for i in nums:
            try:
                d[i]+=1
            except:
                d[i]=1
        for i in d.keys():
            if d[i]>majority:
                return i
