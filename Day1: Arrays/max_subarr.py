'''
Problems url:- https://leetcode.com/problems/maximum-subarray/
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs = -float('inf')
        sums = 0
        for i in range(len(nums)):
            sums+= nums[i]
            if sums>maxs:
                maxs = sums
            if sums<0:
                sums = 0
        return maxs
