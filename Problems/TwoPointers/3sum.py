from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        prev_n = None
        prev_n2 = None

        for i in range(len(nums) - 2):
            if prev_n == nums[i]:
                continue

            prev_n = nums[i]
            seen = {}

        return ans


sol = Solution()
print(sol.threeSum([1, 2, -2, -1]))
