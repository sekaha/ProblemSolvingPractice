from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def recursive(remaining, start=0):
            if remaining == 0:
                return [[]]

            paths = []

            prev_c = None

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                # don't explore duplicate routes
                if candidates[i] == prev_c:
                    continue

                prev_c = candidates[i]

                paths += [
                    [candidates[i]] + path
                    for path in recursive(remaining - candidates[i], i + 1)
                ]

            return paths

        return recursive(target)


sol = Solution()
print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
