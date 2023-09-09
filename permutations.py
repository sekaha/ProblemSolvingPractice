from typing import List

class Solution: 
    def permute(self, nums: List[int]) -> List[List[int]]:   
        permutations = []

        def nested_helper(n, depth=0, indices = []):
            if n == depth:
                permutations.append([nums[i ] for i in indices])
            else:
                for i in range(n):
                    if i not in indices:
                        nested_helper(n,depth+1,indices+[i])

        nested_helper(len(nums))
        return permutations

sol = Solution()
print(sol.permute([0,1]))