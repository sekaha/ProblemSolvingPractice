from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        offsets = [(1,0),(0,1),(-1,0),(0,-1)]
        current_area = 0
        max_area = 0

        def flood_fill(x,y): 
            nonlocal current_area
            grid[x][y] = 0
            current_area += 1

            for x_off, y_off in offsets:
                if (0 < x+x_off < len(grid)) and (0 < y+y_off < len(grid[0])):
                    if grid[x+x_off][y+y_off]:
                        flood_fill(x+x_off,y+y_off)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]:
                    flood_fill(x,y)
                    max_area = max(current_area,max_area)
                    current_area = 0
        
        return max_area

sol = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(sol.maxAreaOfIsland(grid))