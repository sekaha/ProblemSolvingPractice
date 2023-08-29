class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest = prices[0]
        highest = prices[0]
        profit = 0

        for i in range(1,len(prices)):
            if lowest > prices[i]:
                lowest = prices[i]
                highest = prices[i]

            if highest < prices[i]:
                highest = prices[i]            

            profit = max(highest-lowest,profit)

        return profit

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))