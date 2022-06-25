'''
Problem url:- https://leetcode.com/problems/merge-intervals/
First sort the array then traverse the array to find the min max and store then in another list.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = []
        mins,maxs = -1,-1
        intervals.sort(key= lambda x:x[0])
        for i in range(len(intervals)):
            if mins==-1 and maxs==-1:
                mins = intervals[i][0]
                maxs = intervals[i][1]
            else:
                if intervals[i][0]<=maxs:
                    maxs = max(maxs,intervals[i][1])
                    continue
                else:
                    l.append([mins,maxs])
                    mins = intervals[i][0]
                    maxs = intervals[i][1]
        l.append([mins,maxs])
        return l
