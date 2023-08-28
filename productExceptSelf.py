from typing import List
from functools import reduce
from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            result.append(reduce(mul,nums[:i]+nums[i+1:],1))

        return result

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))