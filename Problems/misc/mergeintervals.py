from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ordered = sorted(intervals,key=lambda x: x[0])
        out = [ordered[0]]

        for start, end in ordered[1:]:
            # if this interval started before the last one ended, there is overlap
            if start <= out[-1][1]:
                out[-1][1] = max(end,out[-1][1]) # this is important for events that can be entirely contained within another
            else:
                out.append([start,end])
        
        return out

sol = Solution()
sol.merge([[15,18],[1,3],[2,6],[8,10]])
sol.merge([[1,4],[2,3]])