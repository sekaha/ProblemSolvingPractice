from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        low = 0
        high = 0
        sub_sum = nums[1]
        max_sum = sub_sum

        for i in range(len(nums)):
            if nums[i] > max_sum:
                low = i
                sub_sum = 0
            sub_sum += nums[i]

            if sub_sum > max_sum:
                high = i
                max_sum = sub_sum

        # this is not the optimal way, but I wanted to keep in tact the ARRAY thinking, anyways I'll write a better solution now
        return sum(nums[low : high + 1])


sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
