import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []

        for n in nums:
            heapq.heappush(h, n)

            if len(h) > k:
                heapq.heappop(h)

        return heapq.heappop(h)


sol = Solution()
print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))
