from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # ordering it
        for j in range(2):
            for i, n in enumerate(nums):
                if n == len(nums):
                    swap_v = nums[-1]
                    nums[-1], nums[i] = n, swap_v
                else:
                    swap_v = nums[n]
                    nums[n], nums[i] = n, swap_v
                print(nums)

        for i, n in enumerate(nums):
            if n != i:
                return i

        return len(nums)


sol = Solution()
print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
