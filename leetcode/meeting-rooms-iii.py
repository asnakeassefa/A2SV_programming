class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        print(meetings)
        room = [i for i in range(n)]
        order = []
        store = defaultdict(int)
        for meeting in meetings:
            while order and order[0][0] <= meeting[0]:
                temp = heappop(order)[1]
                heappush(room,temp)
                store[temp] += 1
            if room:
                idx = heappop(room)
                heappush(order,(meeting[1],idx))
            else:
                val = heappop(order)
                store[val[1]] += 1
                time = val[0] + meeting[1] - meeting[0]
                heappush(order,(time,val[1]))
        while order:
            idx = heappop(order)[1]
            store[idx] += 1
        max_ = 0
        ans = 0
        for key,val in store.items():
            if val > max_:
                ans = key
                max_ = val
            elif val == max_:
                ans = min(ans,key)
        print(store)
        return ans