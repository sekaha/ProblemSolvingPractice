from typing import List
import numpy as np


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        for y in range(N // 2):
            for x in range(y, N - y - 1):
                first = matrix[y][x]
                matrix[y][x] = matrix[-x - 1][y]
                matrix[-x - 1][y] = matrix[-y - 1][-x - 1]
                matrix[-y - 1][-x - 1] = matrix[x][-y - 1]
                matrix[x][-y - 1] = first


sol = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol.rotate(matrix)
