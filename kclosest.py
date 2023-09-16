from typing import List
from heapq import heapify, heappop


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = [((x**2 + y**2) ** 0.5, x, y) for x, y in points]
        heapify(self.heap)
        return [heappop(self.heap)[1:3] for i in range(k)]


sol = Solution()
print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
# print(sol.kClosest([[6, 10], [-3, 3], [-2, 5], [0, 2]], 3))
