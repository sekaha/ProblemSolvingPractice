from typing import (
    List,
)

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    # omg.... o(n log n). Then you do O(n)... so we consider this o(n log n) FASCINATING

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i != j: # these are the same meetings
                    m1s, m1e = intervals[i].start, intervals[i].end
                    m2s, m2e = intervals[j].start, intervals[j].end

                    if m2s < m1s < m2e:
                        return False
                    elif m2s < m1e < m2e:
                        return False
        return True

sol = Solution()
print(sol.can_attend_meetings([(5,8),(9,15)]))