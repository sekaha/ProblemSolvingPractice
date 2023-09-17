from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            n, m = numbers[i], numbers[j]

            if n + m == target:
                return [i + 1, j + 1]

            if n + m < target:
                i += 1
            else:
                j -= 1


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
