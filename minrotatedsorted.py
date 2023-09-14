from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        shift = 1

        while l <= r:
            m = (l + r) // 2

            # shift left if it's greater than the current min, to work towards the min
            if nums[m] < res:
                r = m - 1
            else:
                l = m + 1
            res = min(res, nums[m])
            print(res)
        return res


sol = Solution()
sol.findMin([18, 11, 13, 15, 17])
