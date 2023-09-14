from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def helper(candidates, summation=0, path=[]):
            if summation == target:
                yield path

            for i, n in enumerate(candidates):
                if n + summation <= target:
                    yield from helper(candidates[i:], summation + n, path + [n])
                else:
                    break

        return list(helper(candidates))


sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
