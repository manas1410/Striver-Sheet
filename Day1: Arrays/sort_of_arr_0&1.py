'''
problem Url: - https://leetcode.com/problems/sort-colors/
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        v = 0
        l = 0 
        for i in range(3):
            j=v
            while(j<len(nums)):
                if nums[j]==l:
                    nums[j],nums[v] = nums[v],nums[j]
                    v+=1 
                j+=1
            l+=1
