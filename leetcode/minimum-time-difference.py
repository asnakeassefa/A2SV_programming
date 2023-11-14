class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = []
        for timePoint in timePoints:
            h,m = map(int,timePoint.split(':'))
            minute = h * 60 + m
            time.append(minute)
        ans = float('inf')
        length = len(timePoints)
        store = set(time)
        print(time, store)
        if len(store) != len(time):
            return 0
        for i in range(length):
            ptr = 1
            while (time[i] - ptr) % (24*60) not in store and (time[i] + ptr)  % (24 * 60)not in store:   
                ptr += 1
            ans = min(ans,ptr)
        return ans
