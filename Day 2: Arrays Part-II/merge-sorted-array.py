'''
problem url :- https://leetcode.com/problems/merge-sorted-array/s
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n!=0:
            for i in range(m):
                if nums1[i]>nums2[0]:
                    nums1[i],nums2[0] = nums2[0],nums1[i]
                    nums2.sort()
            j = 0
            for i in range(m,m+n):
                nums1[i] = nums2[j]
                j+=1
