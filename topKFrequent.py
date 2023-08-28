class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            # oooo w/ get() you can set default value to zero if it doesn't exist :0
            count[n] = 1 + count.get(n, 0)

        # dict.items() returns the pairs! v convenient
        for n, c in count.items():
            buckets[-c].append(n)

        output = []

        for bucket in buckets:
            for item in bucket:
                output.append(item)
            
            if len(output) == k:
                return output

        # This is O(n) (because it's O(2n))   

sol = Solution()

print(sol.topKFrequent([1,1,1,2,2,3],2))