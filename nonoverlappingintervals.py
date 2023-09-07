from typing import List

class Solution:
    # We must do a greedy solution! 
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ordered = sorted(intervals, key=lambda x : x[1])
        removals = 0
        #conflicts = [[] for i in range(len(ordered))]

        while i < (len(ordered)-1):
            start, end = ordered[i]
            next_start, next_end = ordered[i+1]

            # overlap:
            if next_start < end:
                removals += 1
                # remove one with latest end, to minimize chances of another overlap
                if end < next_end:
                    ordered.remove(ordered[i+1])
                else:
                    ordered.remove(ordered)
            else:
                i+=1

            

        #for i, (start, end) in enumerate(ordered[:-1]):
        #    if 

        # determining interval conflicts
        #for i, (start, end) in enumerate(ordered):
        #    next_interval = i+1
#
        #    # repeated overlap checking
        #    while next_interval < len(ordered) and ordered[next_interval][0] < end:
        #        conflicts[i].append(next_interval)
        #        conflicts[next_interval].append(i)
        #        next_interval += 1
#
        ## greedy ig
        #while sum([len(c) for c in conflicts]):
        #    for c in conflicts:
        #        # remove one with largest end time
        
        


sol = Solution()
print(sol.eraseOverlapIntervals([[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]))