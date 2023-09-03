from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        # build heap, aka heapify down to the leaf nodes (nodes/2)
        for i in range(len(self.nums)//2-1,-1,-1):
            self.heapify(self.nums,i)

    def heapify(self,arr,i):
        # get left and right child indices
        l, r = 2*i+1, 2*i + 2
        largest = i

        # set largest element
        if len(arr) > l:
            if arr[l] > arr[largest]:
                largest = l
        
        if len(arr) > r:
            if arr[r] > arr[largest]:
                largest = r

        # swap largest element and current element
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            self.heapify(arr, largest)

    def heapify_up(self, arr, i):
        parent = (i-1) // 2

        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            
            if parent > 0:
                self.heapify_up(arr,parent)

    def add(self, val: int) -> int:
        # heapify newly inserted element at end of list
        self.nums.append(val)
        self.heapify_up(self.nums,len(self.nums)-1)

        return self.nums[self.k-1]

kthLargest = KthLargest(3, [4, 5, 8, 2])

print(kthLargest.add(3))  # return 4
print(kthLargest.add(5))  # return 5
print(kthLargest.add(10)) # return 5
print(kthLargest.add(9))  # return 8
print(kthLargest.add(4))  # return 8

