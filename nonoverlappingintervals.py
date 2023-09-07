from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ordered = sorted(intervals, key=lambda x : x[0])
        conflicts = [[] for i in range(len(intervals))]

        # determining interval conflicts
        for i, (start, end) in enumerate(ordered):
            next_interval = i+1

            # repeated overlap checking
            while next_interval < len(ordered) and ordered[next_interval][0] < end:
                conflicts[i].append(next_interval)
                conflicts[next_interval].append(i)
                next_interval += 1
        
        # while there's conflicts, remove intervals starting from one with most conflicts
        conflict_counts = [len(c) for c in conflicts]
        removed = 0


        # removing conflicts until we are conflict free
        while sum(conflict_counts):
            removed += 1

            # determine best interval to remove by getting the intervals with the most conflicts and in the case of ties, removing the one that removes the most conflicts "recursively"
            candidates = [i for i, c in enumerate(conflict_counts) if c == max(conflict_counts)]
            print(,candidates)
            min_conflicts = 10**5
            best_candidate = -1

            for candidate in candidates:
                tmp_conflicts = conflicts.copy()
                print(tmp_conflicts)

                # removing conflicts from conflicting cells
                for c in tmp_conflicts[candidate]:
                    tmp_conflicts[c].remove(candidate)

                candidate_conflicts = sum(len(c) for c in tmp_conflicts)

                # if this is the best candidate note it as such and us it
                if candidate_conflicts < min_conflicts:
                    min_conflicts = candidate_conflicts
                    best_candidate = candidate

            # removing conflicts from conflicting cells
            for c in conflicts[best_candidate]:
                conflicts[c].remove(best_candidate)

            # then "removing" self from intervals list
            conflicts[best_candidate] = []
            conflict_counts = [len(c) for c in conflicts]

        return removed

sol = Solution()
print(sol.eraseOverlapIntervals([[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]))