from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ret = len(nums)
        i = 0

        for i in range(len(nums)):
            while nums[i] < len(nums) and nums[i] != nums[nums[i]]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

            if nums[i] == len(nums):
                ret = i

        return ret


sol = Solution()
print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
