from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = lambda a, b: abs(points[a][0] - points[b][0]) + abs(
            points[a][1] - points[b][1]
        )

        # triangle numbers basically, find all coordinate pairs
        costs = {
            (v1, v2): dist(v1, v2)
            for v1 in range(len(points))
            for v2 in range(v1 + 1, len(points))
        }

        print(costs)

        # prims!
        # an indice set that represents the MST
        mst = set()
        total_cost = 0
        min_heap = [[0, 0]]  # [cost, point]

        # BFS
        while len(mst) < len(points):
            # why is the heap important??
            cost, v1 = heapq.heappop(min_heap)

            if v1 in mst:
                continue
            total_cost += cost

            mst.add(v1)

            for v2 in range(len(points)):
                if v2 not in mst:
                    heapq.heappush(min_heap, [costs[min(v1, v2), max(v1, v2)], v2])

        return total_cost


sol = Solution()
print(sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
