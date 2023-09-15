from typing import List

class Solution: 
    def permute(self, nums: List[int]) -> List[List[int]]:   
        permutations = []

        def backtrack(nums, path=[]):
            if not nums: # base case
                permutations.append(path)
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], path + [nums[i]])

        backtrack(nums)
        return permutations

sol = Solution()
print(sol.permute([1,2,3]))