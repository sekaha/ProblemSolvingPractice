from typing import List

class Solution:
    # We must do a greedy solution! 
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ordered = sorted(intervals, key=lambda x : x[1])
        removals = 0

        
sol = Solution()
print(sol.eraseOverlapIntervals([[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]))