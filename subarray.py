from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_sum = nums[1]
        max_sum = sub_sum

        for n in nums[1:]:
            sub_sum = max(n, sub_sum + n)
            max_sum = max(max_sum, sub_sum)

        # this is not the optimal way, but I wanted to keep in tact the ARRAY thinking, anyways I'll write a better solution now
        return max_sum


sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
