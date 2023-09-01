class Solution(object):
    def trap(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        water = [10**5+1]*len(heights)
        l_max = 0
        r_max = 0

        for i in range(len(heights)):
            r_i = len(heights)-i-1
            l_max = max(l_max,heights[i])
            r_max = max(r_max,heights[r_i])

            water[i] = min(water[i],l_max-heights[i])
            water[r_i] = min(water[r_i],r_max-heights[r_i])

        return sum(water)

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))