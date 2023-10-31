class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []

        def heapify_down(i):
            smallest = i

            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(heap):
                if heap[left] < heap[smallest]:
                    smallest = left

                if right < len(heap):
                    if heap[right] < heap[smallest]:
                        smallest = right

                if smallest != i:
                    heap[smallest], heap[i] = heap[i], heap[smallest]
                    heapify_down(smallest)

        def heapify_up(i):
            parent = (i - 1) // 2

            if heap[i] < heap[parent]:
                heap[i], heap[parent] = heap[parent], heap[i]

                if parent > 0:
                    heapify_up(parent)

        def heappush(n):
            heap.append(n)
            heapify_up(len(heap) - 1)

        def heappop():
            heap[-1], heap[0] = heap[0], heap[-1]
            ret = heap.pop()
            heapify_down(0)

            return ret

        for n in nums:
            heappush(n)

            if len(heap) > k:
                heappop()

        return heappop()


sol = Solution()
print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
