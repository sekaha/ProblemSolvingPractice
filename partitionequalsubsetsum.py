from typing import List


class Solution:
    def canpartition(self, nums: List[int]) -> bool:
        # what num we're on in the list
        # which list was last added to
        part1, part2 = [], []
        stack = [(0, 0)]

        while stack:
            i, seen = stack.pop()

            if i == len(nums):
                if sum(part1) == sum(part2):
                    return True
            else:
                if seen == 0:
                    part1.append(nums[i])
                elif seen == 1:
                    part2.append(nums[i])
                    part1.pop()
                elif seen == 2:
                    part2.pop()

                if seen < 2:
                    stack.append((i, seen + 1))

                stack.append((i + 1, 0))

        return False


sol = Solution()
print(sol.canpartition([1, 5, 11, 5]))
