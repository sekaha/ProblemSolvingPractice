from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

        for i in range(len(self.nums),-1,-1):
            self.heapify_down(self.nums,i)

    def heapify_down(self,nums,i):
        l, r = i*2+1, i*2+2
        largest = i

        if l < len(nums):
            if nums[l] < nums[largest]:
                largest = l

        if r < len(nums):
            if nums[r] < nums[largest]:
                largest = r

        if largest != i:
            # swap and recurse up
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapify_down(nums, largest)
        
    def heapify_up(self,nums,i):
        parent = (i-1)//2

        if nums[i] < nums[parent]:
            nums[i], nums[parent] =  nums[parent], nums[i]

            if parent > 0:
                self.heapify_up(nums,parent)

    def add(self, val: int) -> int:
        self.nums.append(val)

        print(self.nums)
        self.heapify_up(self.nums,len(self.nums)-1)
        print(self.nums)

        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))   # return 4
print(kthLargest.add(5))   # return 5
print(kthLargest.add(10))  # return 5
print(kthLargest.add(9))   # return 8
print(kthLargest.add(4))   # return 8