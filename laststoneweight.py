class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            x, y = 0, 0
            
            # find two heaviest stones
            for s in stones:
                if s >= y:
                    x = y
                    y = s
                elif s >= x:
                    x = s

            # smash them together
            if x == y:
                stones.remove(x)
                stones.remove(y)
            else:
                stones.remove(x)
                stones[stones.index(y)] = y-x
        
        return stones[0] if len(stones) == 1 else 0