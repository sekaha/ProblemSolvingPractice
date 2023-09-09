from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = stones

        # build max heap
        for i in range(len(stones)//2 -1, -1, -1):
            self.heapify_down(i)

        while len(self.stones) > 1:
            # smash until one or zero rocks left
            y = self.heap_pop()
            x = self.heap_pop()

            if y != x:
                self.heap_push(y-x)

        return self.stones[0] if self.stones else 0

    def heapify_down(self,i):
        l, r = 2*i + 1, 2*i + 2
        max_i = i

        for j in l, r:
            if j < len(self.stones):
                if self.stones[max_i] < self.stones[j]:
                    max_i = j
        
        if max_i != i:
            self.stones[max_i], self.stones[i] = self.stones[i], self.stones[max_i]
            self.heapify_down(max_i)

    # log n time!
    def heap_pop(self):
        val = self.stones[0]
        self.stones[0] = self.stones[len(self.stones)-1]
        self.stones = self.stones[:-1]
        self.heapify_down(0)

        return val
    
    # log n time!
    def heap_push(self,val):
        self.stones.append(val)
        self.heapify_up(len(self.stones)-1)

    def heapify_up(self,i):
        par = (i-1)//2

        if par >= 0:
            if self.stones[par] < self.stones[i]:
                self.stones[par], self.stones[i] = self.stones[i], self.stones[par]
                self.heapify_up(par)

sol = Solution()
print(sol.lastStoneWeight([1,3]))