from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        combo_sum = set([0])

        for n in nums:
            for combo in combo_sum.copy():
                if combo + n == target:
                    return True
                combo_sum.add(combo + n)
        return False


sol = Solution()
print(sol.canPartition([1, 5, 11, 5]))
