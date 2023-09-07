from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ordered = sorted(intervals, key=lambda x : x[0])
        conflicts = [[] for i in range(len(intervals))]

        for i, (start, end) in enumerate(ordered):
            conflicts = 0
            next_interval = i

            while next_interval < len(ordered) and ordered[next_interval][0] < end:
                conflicts[i].append()