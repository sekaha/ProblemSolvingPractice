from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(candidates, remaining):
            if remaining == 0:
                return [[]]

            results = []

            for i, n in enumerate(candidates):
                if n > remaining:
                    break

                results += [
                    [n] + sub for sub in backtrack(candidates[i:], remaining - n)
                ]

            return results

        return backtrack(candidates, target)


sol = Solution()
print(sol.combinationSum([2, 3, 5], 8))
