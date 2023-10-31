from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.mh = nums
        self.k = k

        print(self.mh)
        for i in range(len(self.mh)//2-1,-1,-1):
            self.heapify_down(i)
        
    def heapify_down(self,i):
        l, r = i*2+1, i*2+2
        least = i

        if l < len(self.mh):
            if self.mh[l] < self.mh[least]:
                least = l

        if r < len(self.mh):
            if self.mh[r] < self.mh[least]:
                least = r

        if least != i:
            # swap and recurse up
            self.mh[i], self.mh[least] = self.mh[least], self.mh[i]
            self.heapify_down(least)
        
    def heapify_up(self,i):
        parent = (i-1)//2

        if self.mh[i] < self.mh[parent]:
            self.mh[i], self.mh[parent] =  self.mh[parent], self.mh[i]

            if parent > 0:
                self.heapify_up(parent)

    def add(self, val: int) -> int:
        self.mh.append(val)
        self.heapify_up(len(self.mh)-1)

        while len(self.mh) > self.k:
            self.mh[0] = self.mh[len(self.mh)-1]
            self.mh = self.mh[:-1]
            self.heapify_down(0)
        
        return self.mh[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, self.mh)
# param_1 = obj.add(val)
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))   # return 4
print(kthLargest.add(5))   # return 5
print(kthLargest.add(10))  # return 5
print(kthLargest.add(9))   # return 8
print(kthLargest.add(4))   # return 8