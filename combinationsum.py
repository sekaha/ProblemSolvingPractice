from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def recursive(target):
            if target == 0:
                return [[]]

            paths = []

            for i, candidate in enumerate(candidates):
                if candidate <= target:
                    next_candidates = candidates[i + 1 :]
                    for path in combination_sum(next_candidates, target - candidate):
                        paths.append([candidate] + path)

            return paths

        return recursive(target)


sol = Solution()
print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
