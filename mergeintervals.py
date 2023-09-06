from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ordered = sorted(intervals,key=lambda x: x[0])
        start_time, end_time = ordered[0][0], ordered[0][1]
        output = []

        for i, (start, end) in enumerate(ordered):
            # if it wasn't merged with the last element and is also the last element
            if i == (len(ordered)-1) and end_time != end:
                output.append((ordered[-1]))
            else:
                end_time = end
                # if this one ends after the next interval starts
                if end > ordered[i+1][0]:
                    end_time = ordered[i+1][1]
                else:
                    output.append([start_time,end_time])
                    start_time = ordered[i+1][0]

        print(output)

sol = Solution()
sol.merge([[15,18],[1,3],[2,6],[8,10]])