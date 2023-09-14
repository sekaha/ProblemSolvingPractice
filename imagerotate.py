from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        for y in range(N):
            for x in range(y + 1, N):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

        for y in range(N):
            for x in range(N // 2):
                matrix[y][x], matrix[y][N - x - 1] = matrix[y][N - x - 1], matrix[y][x]


sol = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol.rotate(matrix)
print(matrix)
