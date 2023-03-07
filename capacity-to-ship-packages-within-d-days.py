class Solution:

    def daysCount(self,arr,k):
        subarray = 1
        Sum = 0
        for num in arr:
            if Sum + num > k:
                subarray += 1
                Sum = 0
            Sum += num
        return subarray
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = low + (high - low) //2
            if self.daysCount(weights,mid) > days:
                low = mid + 1
            elif self.daysCount(weights,mid) <= days:
                high = mid - 1
        return low