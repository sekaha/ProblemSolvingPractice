from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # this must run in O(n) time.... jfc
        # oh so this solution is O(2n)! I see ig?!??!?!
        seen = set(nums)
        length, longest = 1, 0

        for n in nums:
            if (n-1) not in seen:
                next_n = n+1
                
                while (next_n) in seen:
                    length += 1
                    next_n += 1
                longest = max(longest,length)
                length = 1
        
        return longest
        print(longest)

sol = Solution()
sol.longestConsecutive(([0,3,7,2,5,8,4,6,0,1]))