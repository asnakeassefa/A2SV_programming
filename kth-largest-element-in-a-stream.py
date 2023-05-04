class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        length = len(nums)
        for i in range(length-k):
            heapq.heappop(nums)
        self.nums = nums
        self.k = k
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums,val)
        elif val > self.nums[0]:
            heapq.heappushpop(self.nums,val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)