from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest = 0

        i, j = 0, len(height) - 1

        while i < j:
            area = (j - i) * min(height[i], height[j])
            largest = max(area, largest)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return largest


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
