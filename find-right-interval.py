class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        nums = defaultdict(lambda:-1)
        nums1 = []
        nums2 = []

        for i,interval in enumerate(intervals):
            nums[interval[0]] = i
            nums1.append(interval[0])
            nums2.append(interval[1])
        nums1.sort()
        ans = []
        Min = min(nums1)
        Max = max(nums1)

        for num in nums2:
            low = 0
            high = len(nums1) - 1
            while low <= high:
                mid = low + (high - low)//2
                if nums1[mid] < num:
                    low = mid + 1
                elif nums1[mid] >= num:
                    high = mid - 1
            # print(low)
            if low == len(nums1):
                ans.append(-1)
            else:
                ans.append(nums[nums1[low]])
        return ans