from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(candidates, remaining, path=[]):
            if remaining == 0:
                yield path

            for i, n in enumerate(candidates):
                if n > remaining:
                    break
                yield from backtrack(candidates[i:], remaining - n, path + [n])

        return list(backtrack(candidates, target))


sol = Solution()
print(sol.combinationSum([2, 3, 5], 8))
