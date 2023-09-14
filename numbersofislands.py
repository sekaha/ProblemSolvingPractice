from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def check_neighbors(x, y):
            if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == "1":
                grid[y][x] = "0"
                for x_off, y_off in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    check_neighbors(x + x_off, y + y_off)

        for y, row in enumerate(grid):
            for x, land in enumerate(row):
                if land == "1":
                    check_neighbors(x, y)
                    islands += 1

        return islands


sol = Solution()

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

print(sol.numIslands(grid))
