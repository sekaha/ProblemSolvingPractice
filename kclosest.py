from typing import List


class Solution:
    def __init__(self):
        self.heap = []

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = [(x, y, (x**2 + y**2) ** 0.5) for x, y in points]

        # build heap
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

        kclosest = []

        for i in range(k):
            kclosest.append(self.heap_pop())

        return kclosest

    def heapify_down(self, i):
        l, r = i * 2 + 1, i * 2 + 2
        least = i

        if l < len(self.heap):
            if self.heap[l][2] < self.heap[least][2]:
                least = l

        if r < len(self.heap):
            if self.heap[r][2] < self.heap[least][2]:
                least = r

        if i != least:
            self.heap[least], self.heap[i] = self.heap[i], self.heap[least]
            self.heapify_down(least)

    def heap_pop(self):
        smallest = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap = self.heap[:-1]
        self.heapify_down(0)

        return smallest[:2]


sol = Solution()
# print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
print(sol.kClosest([[6, 10], [-3, 3], [-2, 5], [0, 2]], 3))
