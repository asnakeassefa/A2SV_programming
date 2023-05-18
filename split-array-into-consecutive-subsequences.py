class Solution:
    def isPossible(self, nums: List[int]) -> bool: 
        store = []
        i = 0
        length = len(nums)
        while i < length:
            num = nums[i]
            if not store:
                heapq.heappush(store,[num,1])
            else:
                if store[0][0] + 1 == num:
                    val = heapq.heappop(store)
                    heapq.heappush(store,[num,val[1]+1])
                elif store[0][0] == num:
                    heapq.heappush(store,[num,1])
                else:
                    while store and store[0][0] + 1 < num:
                        val = heapq.heappop(store)
                        if val[1] < 3:
                            return False
                    i -= 1
            i += 1
                    
        for value in store:
            if value[1] < 3:
                return False
        return True