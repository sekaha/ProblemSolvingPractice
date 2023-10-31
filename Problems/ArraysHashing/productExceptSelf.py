from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        pre, post = 1, 1

        for i in range(len(nums)):
            result[i] *= pre
            pre  *= nums[i]
            result[len(nums)-i-1] *= post
            post *= nums[len(nums)-i-1]

        return result

sol = Solution()
print(sol.productExceptSelf([-1,1,0,-3,3]))