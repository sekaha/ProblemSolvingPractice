class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        # welp... this is prolly n log n, we can do it a lot faster
        return sorted(counts,key=counts.get)[-k::]


sol = Solution()

print(sol.topKFrequent([1],1))