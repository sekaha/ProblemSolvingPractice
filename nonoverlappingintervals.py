from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ordered = sorted(intervals, key=lambda x : x[0])
        overlaps = [0] * len(intervals)

        for i, (start, end) in enumerate(ordered[1:]):
            # overlap: these intervals start at the same time
            # overlap: previous interval ends after current interval starts
            if (ordered[i-1][0] == start) or (ordered[i-1][1] > start):
                overlaps[i] += 1
                overlaps[i-1] += 1